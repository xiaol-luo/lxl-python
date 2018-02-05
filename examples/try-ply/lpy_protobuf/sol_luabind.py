import lpy_define as ply
import jinja2
import logging
import sys
import codecs
import os

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging

global_lpy_ret = None

def FindMeta(name, search_packages):
    global global_lpy_ret
    for pkg_name in search_packages:
        search_key = name
        if pkg_name:
            search_key = "{}.{}".format(pkg_name, name)
        meta_data = global_lpy_ret.path_node_map.get(search_key, None)
        if meta_data:
            return meta_data
    return None


def IsInternalType(item):
    global global_lpy_ret
    ret = item.meta.path in global_lpy_ret.internal_type_paths
    return ret
        

class EnumFieldEx(object):
    def __init__(self, ply_enum, ply_field):
        self.owner = ply_enum
        self.src = ply_field

    @property
    def tt_name(self):
        return self.src.name

    @property
    def tt_enum_name(self):
        fade_path = "{}.{}".format(self.owner.meta.belong_package, self.owner.meta.name)
        if fade_path == self.owner.meta.path:
            return self.tt_name
        prefix = self.owner.meta.path.replace(self.owner.meta.belong_package, "").strip('.').replace('.', '_')
        return "{}_{}".format(prefix, self.tt_name)
        


class EnumEx(object):
    def __init__(self, ply_enum):
        self.src = ply_enum
        self.meta = self.src
        self.fields = []
        for ply_field in ply_enum.fields:
            field_ex = EnumFieldEx(self, ply_field)
            self.fields.append(field_ex)

    def tt_out_file(self):
        return "LuaBindPB_{}.cpp".format(self.meta.path.replace('.', '_'))

    @property
    def tt_execute_fn_str(self):
        return "LuaBindPB_{0}(L);".format(self.meta.path.replace('.', '_')) 

    @property
    def tt_bind_fn(self):
        ret = "void LuaBindPB_{0}(lua_State *L)".format(self.meta.path.replace('.', '_'))
        return ret

    @property
    def tt_head_file(self):
        return "{}.pb.h".format(self.meta.proto_name)

    @property
    def tt_type(self):
        l = self.meta.path.split('.')
        return l[len(l) - 1]

    @property
    def tt_full_type(self):
        ret = "{}::{}".format(
            self.meta.belong_package.replace(".", "::"), 
            self.meta.path.replace(self.meta.belong_package, "").strip('.').replace('.', '_'))
        return ret

    @property 
    def tt_name_space(self):
        l = self.meta.path.split('.')
        l.pop(len(l) - 1)
        ret = ".".join(l)
        return ret


class NameSpaceEx(object):
    def __init__(self, ply_node):
        self.src = ply_node


class ClassFieldEx(object):
    def __init__(self, class_ex, ply_field):
        self.owner = class_ex
        self.src = ply_field
        self.meta = FindMeta(ply_field.type, class_ex.src.search_packages)
        if not self.meta:
            self.meta = FindMeta(ply_field.type, class_ex.src.search_packages)
            assert(self.meta)

    @property
    def IsInternalType(self):
        global global_lpy_ret
        ret = self.meta.path in global_lpy_ret.internal_type_paths
        return ret

    @property
    def IsString(self):
        if self.IsInternalType and self.meta.name == "string":
            return True
        return False

    @property 
    def IsArray(self):
        return self.src.is_array
    
    @property
    def tt_name(self):
        return self.src.name

    @property
    def IsEnum(self):
        return isinstance(self.meta, ply.PbEnum)

class ClassEx(object):
    def __init__(self, ply_class):
        self.src = ply_class
        self.meta = self.src
        self.fields = []
        for ply_field in ply_class.fields:
            field_ex = ClassFieldEx(self, ply_field)
            self.fields.append(field_ex)
    
    def tt_out_file(self):
        return "LuaBindPB_{}.cpp".format(self.meta.path.replace('.', '_'))

    @property
    def tt_execute_fn_str(self):
        return "LuaBindPB_{0}(L);".format(self.meta.path.replace('.', '_')) 

    @property
    def tt_bind_fn(self):
        ret = "void LuaBindPB_{0}(lua_State *L)".format(self.meta.path.replace('.', '_'))
        return ret

    @property
    def tt_head_file(self):
        return "{}.pb.h".format(self.meta.proto_name)

    @property
    def tt_type(self):
        l = self.meta.path.split('.')
        return l[len(l) - 1]

    @property
    def tt_full_type(self):
        ret = "{}::{}".format(
            self.meta.belong_package.replace(".", "::"), 
            self.meta.path.replace(self.meta.belong_package, "").strip('.').replace('.', '_'))
        return ret

    @property 
    def tt_name_space(self):
        l = self.meta.path.split('.')
        l.pop(len(l) - 1)
        ret = ".".join(l)
        return ret

    @property
    def tt_RepeatedFieldExecuteFn(self):
            return 'PBLuaBindRepeatedPtrField<{}>(L, "", "{}");'.format(self.tt_full_type, self.meta.path.replace('.', '_'))


def GenLuaBindCode(lpy_ret, out_dir):
    global global_lpy_ret
    global_lpy_ret = lpy_ret
    
    out_dir = os.path.abspath(out_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    template_env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        #jinja2.FileSystemLoader("templates")
        jinja2.PackageLoader('lpy_protobuf', 'templates')
    ]))
    
    tt_class = template_env.get_template("sol_pbclass.tt")
    tt_enum = template_env.get_template("sol_pbenum.tt")
    tt_bind = template_env.get_template("sol_bind.tt")

    gen_list = []
    msg_list = []

    for item in global_lpy_ret.path_node_map.values():
        if isinstance(item, ply.PbClass):
            cle = ClassEx(item)
            if not IsInternalType(cle):
                RenderClass(cle, tt_class, out_dir)
                gen_list.append(cle)
                msg_list.append(cle)

        if isinstance(item, ply.PbEnum):
            cee = EnumEx(item)
            RenderEnum(cee, tt_enum, out_dir)
            gen_list.append(cee)

    head_files = set()
    declare_fns = []
    execute_fns = []
    for item in gen_list:
        head_files.add(item.tt_head_file)
        declare_fns.append(item.tt_bind_fn)
        execute_fns.append(item.tt_execute_fn_str)
    tt_ret = tt_bind.render({
        "head_files": head_files,
        "declare_fns": declare_fns,
        "execute_fns": execute_fns,
        "msgs" : msg_list,
    })
    out_file = os.path.join(out_dir, "SolBindProtobuf.cpp") 
    with codecs.open(out_file, 'w', 'utf-8') as f:
        f.write(tt_ret)
    return True


def RenderClass(data, tt, out_dir):
    tt_data = {
        "data" : data 
    }
    tt_ret = tt.render(tt_data)
    log.debug(tt_ret)
    out_file = os.path.join(out_dir, data.tt_out_file()) 
    with codecs.open(out_file, 'w', 'utf-8') as f:
        f.write(tt_ret)


def RenderEnum(data, tt, out_dir):
    tt_data = {
        "data" : data 
    }
    tt_ret = tt.render(tt_data)
    log.debug(tt_ret)
    out_file = os.path.join(out_dir, data.tt_out_file()) 
    with codecs.open(out_file, 'w', 'utf-8') as f:
        f.write(tt_ret)
    
    