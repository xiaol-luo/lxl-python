from .defines import *
import jinja2
import os
import codecs
from clang.cindex import CursorKind

_abspath_relative_path_map = None
_hfile_struct_define_hfile_map = None
_desc_root = None

def find_struct_by_usr(usr):
    global _desc_root
    desc_queue = []
    desc_queue.append(_desc_root)
    while len(desc_queue) > 0:
        desc = desc_queue.pop(0)
        if isinstance(desc, descript_namespace_base):
            desc_queue.extend(desc.structs.values())
            desc_queue.extend(desc.enums)
        if isinstance(desc, descript_namespace):
            desc_queue.extend(desc.namespaces)
        if desc.usr == usr and isinstance(desc, descript_struct):
            return desc
    return None

def _get_relate_path(abspath):
    global _abspath_relative_path_map
    return _abspath_relative_path_map.get(abspath)

def _get_hfile_struct_define_hfile_paths(hfile_path):
    global _hfile_struct_define_hfile_map
    ret = _hfile_struct_define_hfile_map.get(hfile_path)
    return ret or []

class base_meta(object):
    def __init__(self, _desc):
        super(__class__, self).__init__()
        self.desc = _desc

    FILE_PREFIX = "LuaBind"
    FILE_DIR = "cpp"

    @property
    def spelling(self):
        return self.desc.spelling

    @property
    def space_path(self):
        return self.desc.space_path

    @property 
    def full_path(self):
        return self.desc.full_path

    @property 
    def locate_file(self):
        ret = _get_relate_path(self.desc.locate_file)
        return ret

    def out_file_name(self):
        return "{}/{}_{}.cpp".format(base_meta.FILE_DIR, base_meta.FILE_PREFIX, self.full_path.replace('.', '_'))


class enum_meta(base_meta):
    def __init__(self, _desc):
        super(__class__, self).__init__(_desc)
    
    @property
    def name_values(self):
        return self.desc.items


class namespace_meta(base_meta):
    def __init__(self, _desc):
        super(__class__, self).__init__(_desc)

    @property
    def vars(self):
        ret = self.desc.vars
        return ret
    
    @property 
    def fns(self):
        fn_map = {}
        for item in self.desc.funcs:
            fn_map_item = fn_map.get(item.spelling)
            if not fn_map_item:
                fn_map_item = []
                fn_map[item.spelling] = fn_map_item  
            fn_map_item.append(item)
        ret = []
        ret.extend(self.desc.funcs)
        for name, vals in fn_map.items():
            if len(vals) > 1:
                for fn in vals:
                    ret.remove(fn)
        return ret

    @property
    def overload_fns(self):
        fn_map = {}
        for item in self.desc.funcs:
            fn_map_item = fn_map.get(item.spelling)
            if not fn_map_item:
                fn_map_item = []
                fn_map[item.spelling] = fn_map_item  
            fn_map_item.append(item)
        remove_name = []
        for name, vals in fn_map.items():
            if len(vals) <= 1:
                remove_name.append(name)
        for item in remove_name:
            fn_map.pop(item, None)
        ret = []
        for name, vals in fn_map.items():
            fn_str = ""
            for i in range(0, len(vals)):
                fn_elem = vals[i]
                #fn_content = "[]({0}){1},"
                input_str = ""
                excute_str = ""
                for j in range(0, len(fn_elem.params)):
                    param_elem = fn_elem.params[j]
                    input_str += "{} p{},".format(param_elem.type_name, j)
                    excute_str += "p{},".format(j)
                input_str = input_str.strip(',')
                excute_str = excute_str.strip(',')
                excute_fn = fn_elem.full_path.replace(".", "::")
                fn_str += "[]({}){} return {}({}); {},".format(input_str, "{",  excute_fn, excute_str, "}")
            fn_str = fn_str.strip(',')
            overload_str = "sol::overload({})".format(fn_str)
            ret.append({"name": name, "fn_str": overload_str})
        return ret

    @property
    def relate_files(self):
        ret = set()
        if self.locate_file:
            ret.add(self.locate_file)
        if self.desc.locate_file:
            for item in _get_hfile_struct_define_hfile_paths(self.desc.locate_file):
                ret.add(_get_relate_path(item))
        for item in self.desc.funcs:
            relate_path = _get_relate_path(item.locate_file)
            if relate_path:
                ret.add(relate_path)
            if item.locate_file:
                for path in _get_hfile_struct_define_hfile_paths(item.locate_file):
                    ret.add(_get_relate_path(path))
        for item in self.desc.vars:
            relate_path = _get_relate_path(item.locate_file)
            if relate_path:
                ret.add(relate_path)
            if item.locate_file:
                for path in _get_hfile_struct_define_hfile_paths(item.locate_file):
                    ret.add(_get_relate_path(path))
        return ret
        
        
class struct_meta(base_meta):
    def __init__(self, _desc):
        super(__class__, self).__init__(_desc)

    @property
    def is_abstract_struct(self):
        relate_usrs = set()
        wait_check_usrs = [self.desc.usr]
        while wait_check_usrs:
            usr = wait_check_usrs.pop(0)
            relate_usrs.add(usr)
            struct_desc = find_struct_by_usr(usr)
            if struct_desc:
                for item in struct_desc.base_usrs:
                    if item not in relate_usrs:
                        wait_check_usrs.append(item)        
        pure_fns = []
        not_pure_fns = []
        for usr in relate_usrs:
            struct_desc = find_struct_by_usr(usr)
            if not struct_desc:
                continue
            for fn in struct_desc.funcs:
                if fn.is_constructor:
                    continue
                if fn.is_pure:
                    is_append = True
                    for pure_fn in pure_fns:
                        if fn.is_same(pure_fn):
                            is_append = False
                            break
                    if is_append:
                        pure_fns.append(fn)
                else:
                    is_append = True
                    for not_pure_fn in not_pure_fns:
                        if fn.is_same(not_pure_fn):
                            is_append = False
                            break
                    if is_append:
                        not_pure_fns.append(fn)
        for not_pure_fn in not_pure_fns:
            hit_pure_fn = None
            for pure_fn in pure_fns:
                if not_pure_fn.is_same(pure_fn):
                    hit_pure_fn = pure_fn
                    break
            if hit_pure_fn:
                pure_fns.remove(hit_pure_fn)
        return len(pure_fns) > 0

    @property
    def vars(self):
        ret = []
        for item in self.desc.vars:
            if CursorKind.VAR_DECL == item.cursor.kind:
                ret.append(item)
        return ret
    
    @property
    def fields(self):
        ret = []
        for item in self.desc.vars:
            if CursorKind.VAR_DECL != item.cursor.kind:
                ret.append(item)
        return ret

    @property
    def base_classes(self):
        return self.desc.bases

    @property
    def construct_fn_strs(self):
        ret = []
        for fn in self.desc.funcs:
            if not fn.is_constructor:
                continue
            fn_str = self.desc.full_path.replace(".", "::")
            fn_str += "("
            param_count = len(fn.params)
            for i in range(0, param_count):
                fn_str += fn.params[i].type_name
                if i < param_count - 1:
                    fn_str += ", "
            fn_str += ")"
            ret.append(fn_str)
        return ret
        
    def _collect_fns(self, is_overload):
        fns_map = {}
        for fn in self.desc.funcs:
            if fn.is_constructor:
                continue
            fns = fns_map.get(fn.spelling, None)
            if not fns:
                fns = []
                fns_map[fn.spelling] = fns
            fns.append(fn)
        remove_names = []
        for name, fns in fns_map.items():
            fns_len = len(fns)
            if is_overload and fns_len <= 1 or not is_overload and fns_len > 1:
                remove_names.append(name)
        for name in remove_names:
            fns_map.pop(name)
        #remove not public function
        remove_fns_map = {}
        for name, fns in fns_map.items():
            remove_fns = []
            for fn in fns:
                if not fn.is_public:
                    remove_fns.append(fn)
            remove_fns_map[name] = remove_fns
        for name, fns in remove_fns_map.items():
            if len(fns) >= len(fns_map[name]):
                fns_map.pop(name)
                continue
            for fn in fns:
                fns_map[name].remove(fn)
        return fns_map
    
    @property 
    def fns(self):
        fns_map =self._collect_fns(False)
        ret = []
        for fns in fns_map.values():
            ret.append(fns[0])
        return ret
    
    @property
    def overload_fns(self):
        ret = []
        fns_map = self._collect_fns(True)
        for name, fns in fns_map.items():
            #暂时不处理运算符也overload的情况，如果考虑运算符的话需要考虑的东西蛮多的
            if name.startswith("operator"): 
                continue
            fn_name = name
            fn_bind = ""
            fn_wraps = []
            fn_id = 0
            for fn_elem in fns:
                fn_id = fn_id + 1
                input_str = ""
                excute_str = ""
                param_id = 0
                for param_elem in fn_elem.params:
                    param_id = param_id + 1
                    input_str += "{} p{}, ".format(param_elem.type_name, param_id)
                    excute_str += "p{}, ".format(param_id)
                excute_str = excute_str.strip(' ,')
                cls_str = ""
                if not fn_elem.is_static:
                    cls_str = "{}{} &cls, ".format(
                        fn_elem.is_const and "const " or "", 
                        fn_elem.space_path.replace(".", "::")
                    )
                input_str = cls_str + input_str
                input_str = input_str.strip(" ,")
                fn_declare = "static {} {}{}({})".format(
                    fn_elem.return_type,
                    fn_name, 
                    fn_id,
                    input_str
                )
                fn_body = "return {}({});".format(
                    fn_elem.is_static and fn_elem.full_path.replace(".", "::") or "cls.{}".format(fn_elem.spelling),
                    excute_str
                )
                fn_wraps.append({"declare": fn_declare, "body": fn_body})
                fn_bind += "ForOverloadFns::{}{}, ".format(
                    fn_name,
                    fn_id
                )
            fn_bind = "sol::overload({})".format(fn_bind.strip(", "))
            ret.append({"name": fn_name, "bind": fn_bind, "fn_wraps": fn_wraps})
        return ret

    @property
    def relate_files(self):
        ret = set()
        if self.locate_file:
            ret.add(self.locate_file)
        if self.desc.locate_file:
            for item in _get_hfile_struct_define_hfile_paths(self.desc.locate_file):
                ret.add(_get_relate_path(item))
        return ret


def do_render_enum(desc, template_env, outdir):
    tt = template_env.get_template("cpp_enum.tt")
    meta_data = enum_meta(desc)
    ret = tt.render({
        "meta_data": meta_data
    })
    out_file_path = os.path.join(outdir, meta_data.out_file_name())
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    with codecs.open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(ret)
    return True

def do_render_namespace(desc, template_env, outdir):
    meta_data = namespace_meta(desc)
    tt = template_env.get_template("cpp_namespace.tt")
    ret = tt.render({
        "meta_data": meta_data
    })
    out_file_path = os.path.join(outdir, meta_data.out_file_name())
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    with codecs.open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(ret)
    return True

def do_render_struct(desc, template_env, outdir):
    meta_data = struct_meta(desc)
    #if meta_data.is_abstract_struct():
    #    return False
    tt = template_env.get_template("cpp_struct.tt")
    ret = tt.render({
        "meta_data": meta_data
    })
    out_file_path = os.path.join(outdir, meta_data.out_file_name())
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    with codecs.open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(ret)
    return True

render_actions = {
    enum_descript_type.enum: do_render_enum,
    enum_descript_type.namespace: do_render_namespace,
    enum_descript_type.struct: do_render_struct,
}

def do_render(desc_root, abspath_relative_path_map, hfile_struct_define_hfile_map, outdir):
    global _abspath_relative_path_map
    _abspath_relative_path_map = abspath_relative_path_map
    global _hfile_struct_define_hfile_map
    _hfile_struct_define_hfile_map = hfile_struct_define_hfile_map
    global _desc_root
    _desc_root = desc_root
    template_env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        jinja2.PackageLoader(__package__, package_path='templates')
        #jinja2.FileSystemLoader("")
    ]))
    gen_descs = []
    desc_queue = []
    desc_queue.append(desc_root)
    while len(desc_queue) > 0:
        desc = desc_queue.pop(0)
        render_action = render_actions.get(desc.desc_type, None)
        if render_action:
            if render_action(desc, template_env, outdir):
                gen_descs.append(desc)
        if isinstance(desc, descript_namespace_base):
            desc_queue.extend(desc.structs.values())
            desc_queue.extend(desc.enums)
        if isinstance(desc, descript_namespace):
            desc_queue.extend(desc.namespaces)
    # gen bind function
    tt = template_env.get_template("cpp_bind.tt")
    ret = tt.render({
        "descs": gen_descs
    })
    out_file_path = os.path.join(outdir, "{}/{}".format(base_meta.FILE_DIR, "SolBindCommon.cpp"))
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True)
    with codecs.open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(ret)
        