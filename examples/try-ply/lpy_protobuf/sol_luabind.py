import lpy_define as ply
import jinja2
import logging
import sys

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


class ClassFieldEx(object):
    def __init__(self, class_ex, ply_field):
        self.owner = class_ex
        self.src = ply_field
        self.meta = FindMeta(ply_field.type, class_ex.src.search_packages)
        if not self.meta:
            self.meta = FindMeta(ply_field.type, class_ex.src.search_packages)
            assert(self.meta)


class ClassEx(object):
    def __init__(self, ply_class):
        self.src = ply_class
        self.meta = self.src
        self.fields = []
        for ply_field in ply_class.fields:
            field_ex = ClassFieldEx(self, ply_field)
            self.fields.append(field_ex)


class EnumFieldEx(object):
    def __init__(self, ply_enum, ply_field):
        self.owner = ply_enum
        self.src = ply_field

    @property
    def tt_name(self):
        return self.src.name


class EnumEx(object):
    def __init__(self, ply_enum):
        self.src = ply_enum
        self.meta = self.src
        self.fields = []
        for ply_field in ply_enum.fields:
            field_ex = EnumFieldEx(self, ply_field)
            self.fields.append(field_ex)

    @property
    def tt_bind_fn(self):
        ret = "void LuaBindPB_{0}()".format(self.meta.path.replace('.', '_'))
        return ret

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


def GenLuaBindCode(lpy_ret, out_dir):
    global global_lpy_ret
    global_lpy_ret = lpy_ret
    template_env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        #jinja2.FileSystemLoader("templates")
        jinja2.PackageLoader('lpy_protobuf', 'templates')
    ]))
    
    tt_class = template_env.get_template("sol_pbclass.tt")
    tt_enum = template_env.get_template("sol_pbenum.tt")

    for item in global_lpy_ret.path_node_map.values():
        if isinstance(item, ply.PbClass):
            cle = ClassEx(item)
            if not IsInternalType(cle):
                RenderClass(cle, tt_class, out_dir)
        if isinstance(item, ply.PbEnum):
            cee = EnumEx(item)
            RenderEnum(cee, tt_enum, out_dir)
    return True


def RenderClass(data, tt, out_dir):
    pass


def RenderEnum(data, tt, out_dir):
    tt_data = {
        "data" : data
    }
    log.debug(tt.render(tt_data))
    pass
