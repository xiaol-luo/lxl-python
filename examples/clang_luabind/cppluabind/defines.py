from clang.cindex import CursorKind, AccessSpecifier


class base_enum(object):
    """
    Common base class for named enumerations .

    Subclasses must define their own _kinds and _name_map members, as:
    _kinds = []
    _name_map = None
    These values hold the per-subclass instances and value-to-name mappings,
    respectively.

    """

    def __init__(self, value):
        if value >= len(self.__class__._kinds):
            self.__class__._kinds += [None] * (value - len(self.__class__._kinds) + 1)
        if self.__class__._kinds[value] is not None:
            raise ValueError('{0} value {1} already loaded'.format(
                str(self.__class__), value))
        self.value = value
        self.__class__._kinds[value] = self
        self.__class__._name_map = None

    def from_param(self):
        return self.value

    @property
    def name(self):
        """Get the enumeration name of this cursor kind."""
        if self._name_map is None:
            self._name_map = {}
            for key, value in self.__class__.__dict__.items():
                if isinstance(value, self.__class__):
                    self._name_map[value] = key
        return self._name_map[self]

    @classmethod
    def from_id(cls, id):
        if id >= len(cls._kinds) or cls._kinds[id] is None:
            raise ValueError('Unknown template argument kind %d' % id)
        return cls._kinds[id]

    def __repr__(self):
        return '%s.%s' % (self.__class__, self.name,)


### descript type enum ###
class enum_descript_type(base_enum):
    # The required base_enum declarations.
    _kinds = []
    _name_map = None

enum_descript_type.invalid = enum_descript_type(0)
enum_descript_type.namespace = enum_descript_type(1)
enum_descript_type.struct = enum_descript_type(2)
enum_descript_type.function = enum_descript_type(3)
enum_descript_type.variable = enum_descript_type(4)
enum_descript_type.param = enum_descript_type(5)
enum_descript_type.enum = enum_descript_type(6)


class descript_base(object):
    def __init__(self, _desc_type):
        self.parent = None
        self.desc_type = _desc_type
        self.spelling = ""
        self.type_name = ""
        self.cursor = None
        self.usr = None
        self.brief_comment = None

    @property
    def space_path(self):
        ret = ""
        p = self.parent
        while p and isinstance(p, descript_namespace_base):
            ret = "{}.{}".format(p.spelling, ret)
            p = p.parent
        ret = ret.strip('.')
        return ret 

    @property
    def full_path(self):
        ret = "{}.{}".format(self.space_path, self.spelling).strip('.')
        return ret
    
    @staticmethod
    def try_parse_child_ast(cursor, parent_desc, parse_files=None):
        is_public = True
        for child_cursor in cursor.get_children():
            if parse_files and child_cursor.location.file.name.replace('\\', '/') not in parse_files:
                    continue
            cursor_kind = child_cursor.kind
            if  CursorKind.CXX_ACCESS_SPEC_DECL == cursor_kind:
                is_public = AccessSpecifier.PUBLIC == child_cursor.access_specifier
            if not cursor_kind.is_declaration():
                continue
            if False:
                pass
            elif CursorKind.NAMESPACE == cursor_kind:
                descript_namespace.parse_ast(child_cursor, parent_desc)
            elif CursorKind.STRUCT_DECL == cursor_kind or CursorKind.CLASS_DECL == cursor_kind:
                descript_struct.parse_ast(child_cursor, parent_desc)
            elif CursorKind.FIELD_DECL == cursor_kind or CursorKind.VAR_DECL == cursor_kind:
                descript_variable.parse_ast(child_cursor, parent_desc)
            elif CursorKind.FUNCTION_DECL == cursor_kind or CursorKind.CXX_METHOD == cursor_kind \
                    or CursorKind.CONSTRUCTOR == cursor_kind \
                    or CursorKind.FUNCTION_TEMPLATE == cursor_kind:
                descript_function.parse_ast(child_cursor, parent_desc)
            elif CursorKind.PARM_DECL == cursor_kind:
                descript_function_param.parse_ast(child_cursor, parent_desc)
            elif CursorKind.ENUM_DECL == cursor_kind:
                descript_enum.parse_ast(child_cursor, parent_desc)

    @property
    def locate_file(self):
        if self.cursor.location.file:
            return self.cursor.location.file.name.replace('\\', '/')
        return ""

    def fill_common_fields(self, cursor):
        self.spelling = cursor.spelling
        self.type_name = cursor.type.get_canonical().spelling
        self.cursor = cursor
        self.usr = cursor.get_usr()
        self.brief_comment = cursor.brief_comment
        if self.brief_comment:
            self.brief_comment = self.brief_comment.strip(" ")

    def is_ignore(self):
        if not self.brief_comment:
            return False
        if self.brief_comment != "sol_ignore":
            return False
        return True


class descript_enum(descript_base):
    def __init__(self):
        super(__class__, self).__init__(enum_descript_type.enum)
        self.items = []

    @staticmethod
    def parse_ast(cursor, parent_desc):
        elem = descript_enum()
        elem.parent = parent_desc
        if parent_desc:
            assert(isinstance(parent_desc, descript_namespace_base))
            parent_desc.enums.append(elem)
        elem.fill_common_fields(cursor)
        for child_cursor in cursor.get_children():
            if CursorKind.ENUM_CONSTANT_DECL != child_cursor.kind:
                continue
            elem.items.append({"name": child_cursor.spelling, "value": child_cursor.enum_value})
        return elem
    
class descript_variable(descript_base):
    def __init__(self):
        super(__class__, self).__init__(enum_descript_type.variable)
        self.is_const = False

    def is_same(self, other):
        if self.spelling != other.spelling:
            return False
        if self.type_name != other.type_name:
            return False
        return True

    @staticmethod
    def parse_ast(cursor, parent_desc):
        if parent_desc \
            and isinstance(parent_desc, descript_struct) \
            and AccessSpecifier.PUBLIC != cursor.access_specifier:
            return False
        elem = descript_variable()
        elem.fill_common_fields(cursor)
        elem.parent = parent_desc
        
        if parent_desc:
            assert(isinstance(parent_desc, descript_namespace_base))
            parent_desc.vars.append(elem)
        elem.is_const = cursor.type.is_const_qualified()
        #remove same function declare
        if parent_desc:
            for item in parent_desc.vars:
                if item != elem:
                    if item.is_same(elem):
                        parent_desc.vars.remove(elem)
                        break
        return elem


class descript_function_param(descript_base):
    def __init__(self):
        super(__class__, self).__init__(enum_descript_type.param)
    
    def is_same(self, other):
        return self.type_name == other.type_name


    @staticmethod
    def parse_ast(cursor, parent_desc):
        elem = descript_function_param()
        elem.parent = parent_desc
        if parent_desc:
            assert(isinstance(parent_desc, descript_function))
            parent_desc.params.append(elem)
        elem.fill_common_fields(cursor)
        return elem

class descript_function(descript_base):
    def __init__(self):
        super(__class__, self).__init__(enum_descript_type.function)
        self.params = []
        self.return_type = None
        self.is_static = False
        self.is_constructor = False
        self.is_virtual = False
        self.is_const = False
        self.is_pure = False
        self.is_template = False

    def is_same(self, other):
        if self.spelling != other.spelling:
            return False
        if len(self.params) != len(other.params):
            return False
        if self.is_const != other.is_const:
            return False
        if self.is_static != other.is_static:
            return False
        if self.is_template != other.is_template:
            return False
        for i in range(0, len(self.params)):
            if not self.params[i].is_same(other.params[i]):
                return False
        return True

    @property
    def is_public(self):
        if not self.parent or not isinstance(self.parent, descript_struct):
            return True
        return AccessSpecifier.PUBLIC == self.cursor.access_specifier

    @staticmethod
    def parse_ast(cursor, parent_desc):
        elem = descript_function()
        elem.parent = parent_desc
        if parent_desc:
            assert(isinstance(parent_desc, descript_namespace_base))
            parent_desc.funcs.append(elem)
        elem.fill_common_fields(cursor)
        #to do something
        result_type = cursor.type.get_result()
        elem.return_type = cursor.type.get_result().get_canonical().spelling
        elem.is_static = cursor.is_static_method()
        elem.is_constructor = cursor.is_converting_constructor() \
                            or cursor.is_copy_constructor() \
                            or cursor.is_default_constructor() \
                            or cursor.is_move_constructor()
        elem.is_constructor = CursorKind.CONSTRUCTOR == cursor.kind
        elem.is_virtual = cursor.is_pure_virtual_method() or cursor.is_virtual_method()
        elem.is_const = cursor.is_const_method()
        elem.is_pure = cursor.is_pure_virtual_method()
        elem.is_template = CursorKind.FUNCTION_TEMPLATE == cursor.kind
        descript_base.try_parse_child_ast(cursor, elem)
        #remove same function declare
        if parent_desc:
            for item in parent_desc.funcs:
                if item != elem:
                    if item.is_same(elem):
                        parent_desc.funcs.remove(elem)
                        break
        return elem
        


class descript_namespace_base(descript_base):
    def __init__(self, _desc_type):
        super(__class__, self).__init__(_desc_type)
        self.funcs = []
        self.vars = []
        self.structs = {}
        self.enums = []


class descript_struct(descript_namespace_base):
    def __init__(self):
        super(__class__, self).__init__(enum_descript_type.struct)
        self.bases = []
        self.base_usrs = []

    @property
    def is_public(self):
        if AccessSpecifier.PROTECTED == self.cursor.access_specifier or \
            AccessSpecifier.PRIVATE == self.cursor.access_specifier:
            return False
        if self.parent and isinstance(self.parent, descript_struct):
            return self.parent.is_public
        return True 
    
    @staticmethod
    def parse_ast(cursor, parent_desc):
        if not cursor.is_definition():
            return None
        elem = descript_struct()
        elem.parent = parent_desc
        elem.fill_common_fields(cursor)
        if not elem.spelling:
            return None
        if not elem.is_public:
            return None
        old_elem = None
        if parent_desc:
            assert(isinstance(parent_desc, descript_namespace_base))
            old_elem = parent_desc.structs.get(cursor.spelling, None)
            parent_desc.structs[cursor.spelling] = elem
        descript_base.try_parse_child_ast(cursor, elem)
        for child_cursor in cursor.get_children(): #identify base classes
            if CursorKind.CXX_BASE_SPECIFIER == child_cursor.kind:
                if AccessSpecifier.PUBLIC == child_cursor.access_specifier:
                    elem.bases.append(child_cursor.type.get_canonical().spelling)
                elem.base_usrs.append(child_cursor.get_definition().get_usr())
        if old_elem:
            old_weight = len(old_elem.funcs) + len(old_elem.vars) + len(old_elem.structs) + len(old_elem.enums) + len(old_elem.bases)
            new_weight = len(elem.funcs) + len(elem.vars) + len(elem.structs) + len(elem.enums) + len(elem.bases)
            if new_weight > 0 and old_weight > 0:
                assert(False)
            assert(0 == old_weight or 0 == new_weight)
            if old_weight > new_weight:
                parent_desc.structs[old_elem.spelling] = old_elem
        return elem        


class descript_namespace(descript_namespace_base):
    def __init__(self):
        self.namespaces = []
        super(__class__, self).__init__(enum_descript_type.namespace)

    @staticmethod
    def parse_ast(cursor, parent_desc):
        elem = descript_namespace()
        elem.parent = parent_desc
        elem.fill_common_fields(cursor)
        if not elem.spelling:
            return None
        if parent_desc:
            assert(isinstance(parent_desc, descript_namespace))
            is_find = False
            for item in parent_desc.namespaces:
                if item.spelling == elem.spelling:
                    elem = item
                    is_find = True
                    break
            if not is_find:
                parent_desc.namespaces.append(elem)
        descript_base.try_parse_child_ast(cursor, elem)
        return elem

