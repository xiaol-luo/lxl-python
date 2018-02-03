STR_EMPTY = ''

class PbNode(object):
    def __init__(self):
        self.path = STR_EMPTY
        self.name = STR_EMPTY
        self.parent = None
        self.children = {}


class PbClass(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.search_packages = set()
        self.belong_package = STR_EMPTY
        self.proto_name = STR_EMPTY
        self.fields = []

class PbClassField(object):
    def __init__(self):
        self.is_array = False
        self.type = STR_EMPTY
        self.name = STR_EMPTY
        self.filed_id = -1
        self.owner = None

class PbEnum(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.belong_package = STR_EMPTY
        self.proto_name = STR_EMPTY
        self.fields = []


class PbEnumField(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.name = STR_EMPTY
        self.value = -1
        self.owner = None


class YaccResult(object):
    def __init__(self):
        self.syntax = STR_EMPTY
        self.package = STR_EMPTY
        self.imports = set()
        self.options = {}
        self.ns = PbNode()

class LpyResult(object):
    def __init__(self):
        self.path_node_map = {}
        self.Internal_Package = STR_EMPTY
        self.internal_type_paths = set()

def FindPbNode(pb_node, node_path, is_create):
    if not pb_node:
        return None
    node_names = []
    if node_path:
        node_names = node_path.split('.')
    ret_node = pb_node
    for node_name in node_names:
        if not ret_node: break
        finded_node = ret_node.children.get(node_name, None)
        if is_create and not finded_node:
            finded_node = PbNode()
            finded_node.name = node_name
            finded_node.parent = ret_node
            ret_node.children[finded_node.name] = finded_node
        ret_node = finded_node
    return ret_node