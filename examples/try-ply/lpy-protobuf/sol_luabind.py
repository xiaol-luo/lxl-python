import lpy_define as ply

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
        self.fields = []
        for ply_field in ply_class.fields:
            field_ex = ClassFieldEx(self, ply_field)
            self.fields.append(field_ex)

class EnumFieldEx(object):
    def __init__(self, ply_enum, ply_field):
        self.owner = ply_enum
        self.src = ply_field

class EnumEx(object):
    def __init__(self, ply_enum):
        self.src = ply_enum
        self.fields = []
        for ply_field in ply_enum.fields:
            field_ex = EnumFieldEx(self, ply_field)
            self.fields.append(field_ex)

class NameSpaceEx(object):
    def __init__(self, ply_node):
        self.src = ply_node

def GenLuaBindCode(lpy_ret):
    global global_lpy_ret
    global_lpy_ret = lpy_ret
    for item in global_lpy_ret.path_node_map.values():
        if isinstance(item, ply.PbClass):
            cle = ClassEx(item)
        if isinstance(item, ply.PbEnum):
            cee = EnumEx(item)

    return True
