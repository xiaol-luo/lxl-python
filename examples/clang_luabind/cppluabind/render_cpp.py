from .defines import *
import jinja2
import os
import codecs
from clang.cindex import CursorKind

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
        ret = self.desc.funcs
        return ret
        

class struct_meta(base_meta):
    def __init__(self, _desc):
        super(__class__, self).__init__(_desc)

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
        
    @property
    def fns(self):
        ret = []
        for fn in self.desc.funcs:
            if not fn.is_constructor:
                ret.append(fn)
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

def do_render_struct(desc, template_env, outdir):
    meta_data = struct_meta(desc)
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

render_actions = {
    enum_descript_type.enum: do_render_enum,
    enum_descript_type.namespace: do_render_namespace,
    enum_descript_type.struct: do_render_struct,
}


def do_render(desc_root, outdir):
    template_env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        jinja2.PackageLoader(__package__, package_path='templates')
        #jinja2.FileSystemLoader("")
    ]))

    desc_queue = []
    desc_queue.append(desc_root)
    while len(desc_queue) > 0:
        desc = desc_queue.pop(0)
        render_action = render_actions.get(desc.desc_type, None)
        if render_action:
            render_action(desc, template_env, outdir)
        
        if isinstance(desc, descript_namespace_base):
            desc_queue.extend(desc.structs.values())
            desc_queue.extend(desc.enums)
        if isinstance(desc, descript_namespace):
            desc_queue.extend(desc.namespaces)
        