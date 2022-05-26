from ..clang.cindex import CursorKind, AccessSpecifier
import typing


class BaseEnum(object):
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


### desc type enum ###
class Enum_Desc_Type(BaseEnum):
    # The required BaseEnum declarations.
    _kinds = []
    _name_map = None


Enum_Desc_Type.invalid = Enum_Desc_Type(0)
Enum_Desc_Type.namespace = Enum_Desc_Type(1)
Enum_Desc_Type.struct = Enum_Desc_Type(2)
Enum_Desc_Type.function = Enum_Desc_Type(3)
Enum_Desc_Type.variable = Enum_Desc_Type(4)
Enum_Desc_Type.param = Enum_Desc_Type(5)
Enum_Desc_Type.enum = Enum_Desc_Type(6)


class AstDescBase(object):
    def __init__(self, _desc_type):
        self.desc_type = _desc_type
        self.parent = None
        self.cursor = None
        self.spelling = ""
        self.type_name = ""
        self.usr = None
        self.brief_comment = None
        self.is_sol_ignore = False
        self.is_sol_property = False
        self.is_parsed = False

    @property
    def space_path(self):
        ret = ""
        p = self.parent
        while p and isinstance(p, AstDescNamespaceBase):
            ret = "{}.{}".format(p.spelling, ret)
            p = p.parent
        ret = ret.strip('.')
        return ret

    @property
    def full_path(self):
        ret = "{}.{}".format(self.space_path, self.spelling).strip('.')
        return ret

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
            comments = self.brief_comment.split(" ")
            for item in comments:
                if "sol_ignore" == item.strip('/ ').lower():
                    self.is_sol_ignore = True
                    break
            if not self.is_sol_ignore:
                for item in comments:
                    if "sol_property" == item.strip('/ ').lower():
                        self.is_sol_property = True

    def do_parse_ast(self):
        if self.is_parsed:
            return []
        assert self.cursor
        self.is_parsed = True
        return self.do_parse_ast_help()

    def do_parse_ast_help(self):
        return []


class AstDescEnum(AstDescBase):
    def __init__(self):
        super(__class__, self).__init__(Enum_Desc_Type.enum)
        self.items = []

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescNamespaceBase))
            self.parent.enums.append(self)
        self.fill_common_fields(self.cursor)
        for child_cursor in self.cursor.get_children():
            if CursorKind.ENUM_CONSTANT_DECL != child_cursor.kind:
                continue
            self.items.append({"name": child_cursor.spelling, "value": child_cursor.enum_value})
        return []


class AstDescVariable(AstDescBase):
    def __init__(self):
        super(__class__, self).__init__(Enum_Desc_Type.variable)
        self.is_const = False

    def is_same(self, other):
        if self.spelling != other.spelling:
            return False
        if self.type_name != other.type_name:
            return False
        return True

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescNamespaceBase))
            self.parent.vars.append(self)
        self.fill_common_fields(self.cursor)
        self.is_const = self.cursor.type.is_const_qualified()
        return []


class AstDescFunctionParam(AstDescBase):
    def __init__(self):
        super(__class__, self).__init__(Enum_Desc_Type.param)

    def is_same(self, other):
        return self.type_name == other.type_name

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescFunction))
            self.parent.params.append(self)
        self.fill_common_fields(self.cursor)
        return []


class AstDescFunction(AstDescBase):
    def __init__(self):
        super(__class__, self).__init__(Enum_Desc_Type.function)
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
        if not self.parent or not isinstance(self.parent, AstDescStruct):
            return True
        return AccessSpecifier.PUBLIC == self.cursor.access_specifier

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescNamespaceBase))
            self.parent.funcs.append(self)
        self.fill_common_fields(self.cursor)
        self.return_type = self.cursor.type.get_result().get_canonical().spelling
        self.is_static = self.cursor.is_static_method()
        self.is_constructor = self.cursor.is_converting_constructor() \
                              or self.cursor.is_copy_constructor() \
                              or self.cursor.is_default_constructor() \
                              or self.cursor.is_move_constructor()
        self.is_constructor = CursorKind.CONSTRUCTOR == self.cursor.kind
        self.is_virtual = self.cursor.is_pure_virtual_method() or self.cursor.is_virtual_method()
        self.is_const = self.cursor.is_const_method()
        self.is_pure = self.cursor.is_pure_virtual_method()
        self.is_template = CursorKind.FUNCTION_TEMPLATE == self.cursor.kind
        wait_parse_desc_list = _create_child_desc_list(self, self.cursor)
        while wait_parse_desc_list:
            head_desc = wait_parse_desc_list.pop(0)
            child_desc_list = head_desc.do_parse_ast()
            wait_parse_desc_list.extend(child_desc_list)
        return wait_parse_desc_list


class AstDescNamespaceBase(AstDescBase):
    def __init__(self, _desc_type):
        super(__class__, self).__init__(_desc_type)
        self.funcs = []
        self.vars = []
        self.structs = {}
        self.cached_struct_list = []
        self.enums = []


class AstDescStruct(AstDescNamespaceBase):
    def __init__(self):
        super(__class__, self).__init__(Enum_Desc_Type.struct)
        self.bases = []
        self.base_usrs = []

    @property
    def is_public(self):
        if AccessSpecifier.PROTECTED == self.cursor.access_specifier or \
                AccessSpecifier.PRIVATE == self.cursor.access_specifier:
            return False
        if self.parent and isinstance(self.parent, AstDescStruct):
            return self.parent.is_public
        return True

    def cal_weight(self):
        weight = len(self.funcs) + len(self.vars) + len(self.structs) + len(self.enums) + len(self.bases)
        return weight

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescNamespaceBase))
            self.parent.cached_struct_list.append(self)
        self.fill_common_fields(self.cursor)
        for child_cursor in self.cursor.get_children():  # identify base classes
            if CursorKind.CXX_BASE_SPECIFIER == child_cursor.kind:
                if AccessSpecifier.PUBLIC == child_cursor.access_specifier:
                    self.bases.append(child_cursor.type.get_canonical().spelling)
                self.base_usrs.append(child_cursor.get_definition().get_usr())
        wait_parse_desc_list = _create_child_desc_list(self, self.cursor)
        return wait_parse_desc_list


class AstDescNamespace(AstDescNamespaceBase):
    def __init__(self):
        self.namespaces = []
        super(__class__, self).__init__(Enum_Desc_Type.namespace)

    def do_parse_ast_help(self):
        if self.parent:
            assert (isinstance(self.parent, AstDescNamespace))
            self.parent.namespaces.append(self)
        self.fill_common_fields(self.cursor)
        wait_parse_desc_list = _create_child_desc_list(self, self.cursor)
        return wait_parse_desc_list


def parse_ast(top_desc, cursor, parse_files=None):
    all_desc_list = [ top_desc ]
    child_cursor_list = []
    for child_cursor in cursor.get_children():
        need_parse = True
        if parse_files and child_cursor.location.file.name.replace('\\', '/') not in parse_files:
            need_parse = False
        if need_parse:
            child_cursor_list.append(child_cursor)
    wait_parse_desc_list = []
    for child_cursor in child_cursor_list:
        child_desc = _create_desc(top_desc, child_cursor)
        if child_desc:
            wait_parse_desc_list.append(child_desc)
    all_desc_list.extend(wait_parse_desc_list)
    while wait_parse_desc_list:
        head_desc: AstDescBase = wait_parse_desc_list.pop(0)
        child_desc_list = head_desc.do_parse_ast()
        wait_parse_desc_list.extend(child_desc_list)
        all_desc_list.extend(child_desc_list)
    while all_desc_list:
        desc = all_desc_list.pop()
        need_check_desc_list = _fix_desc(desc)
        all_desc_list.extend(need_check_desc_list)


def _fix_desc(desc: AstDescBase):
    if not desc.parent:
        return []

    need_check_desc_list = []
    if Enum_Desc_Type.namespace == desc.desc_type:
        # 合并命名空间
        ns_desc_list = []
        for elem in desc.parent.namespaces:
            if elem != desc and elem.spelling == desc.spelling:
                ns_desc_list.append(elem)
                elem.parent = None
                need_check_desc_list.extend(elem.namespaces)
                need_check_desc_list.extend(elem.funcs)
                need_check_desc_list.extend(elem.vars)
                need_check_desc_list.extend(elem.enums)
                need_check_desc_list.extend(elem.structs.values())
                desc.namespaces.extend(elem.namespaces)
                desc.funcs.extend(elem.funcs)
                desc.vars.extend(elem.vars)
                desc.enums.extend(elem.enums)
                if elem.structs:
                    if desc.cached_struct_list is None:
                        desc.cached_struct_list = []
                    desc.cached_struct_list.extend(elem.structs.values())
                for x in elem.namespaces: x.parent = desc
                for x in elem.funcs: x.parent = desc
                for x in elem.vars: x.parent = desc
                for x in elem.enums: x.parent = desc
                for x in elem.structs.values(): x.parent = desc
        for elem in ns_desc_list:
            desc.parent.namespaces.remove(elem)
    if Enum_Desc_Type.struct == desc.desc_type:
        # 根据权限，删掉重名的struct
        win_all = True
        desc_weight = desc.cal_weight()
        for elem in desc.parent.cached_struct_list:
            if desc != elem and desc.spelling == elem.spelling and elem.cal_weight() > desc_weight:
                win_all = False
                break
        if win_all and desc.spelling not in desc.parent.structs:
            desc.parent.structs[desc.spelling] = desc
        desc.parent.cached_struct_list.remove(desc)
    if Enum_Desc_Type.function == desc.desc_type:
        # 删掉is_same的函数
        for elem in desc.parent.funcs:
            if elem != desc and desc.is_same(elem):
                desc.parent.funcs.remove(desc)
                break
    if Enum_Desc_Type.variable == desc.desc_type:
        # 删掉同名的变量
        for elem in desc.parent.vars:
            if elem != desc and desc.is_same(elem):
                desc.parent.vars.remove(desc)
    if Enum_Desc_Type.param == desc.desc_type:
        pass
    if Enum_Desc_Type.enum == desc.desc_type:
        pass
    return need_check_desc_list


def _create_desc(parent_desc: AstDescBase, child_cursor) -> typing.Optional[AstDescBase]:
    cursor_kind = child_cursor.kind
    ret_desc = None
    if not cursor_kind.is_declaration():
        pass
    elif CursorKind.NAMESPACE == cursor_kind:
        if child_cursor.spelling:
            ret_desc = AstDescNamespace()
    elif CursorKind.STRUCT_DECL == cursor_kind or CursorKind.CLASS_DECL == cursor_kind:
        if child_cursor.is_definition() and child_cursor.spelling:
            ret_desc = AstDescStruct()
    elif CursorKind.FIELD_DECL == cursor_kind or CursorKind.VAR_DECL == cursor_kind:
        ret_desc = AstDescVariable()
    elif CursorKind.FUNCTION_DECL == cursor_kind or CursorKind.CXX_METHOD == cursor_kind \
            or CursorKind.CONSTRUCTOR == cursor_kind \
            or CursorKind.FUNCTION_TEMPLATE == cursor_kind:
        ret_desc = AstDescFunction()
    elif CursorKind.PARM_DECL == cursor_kind:
        ret_desc = AstDescFunctionParam()
    elif CursorKind.ENUM_DECL == cursor_kind:
        AstDescEnum.parse_ast(child_cursor, parent_desc)
        ret_desc = AstDescEnum()
    if ret_desc:
        ret_desc.cursor = child_cursor
        ret_desc.parent = parent_desc
    return ret_desc


def _create_child_desc_list(parent_desc, cursor):
    ret_desc_list = []
    for child_cursor in cursor.get_children():
        child_desc = _create_desc(parent_desc, child_cursor)
        if child_desc:
            ret_desc_list.append(child_desc)
    return ret_desc_list
