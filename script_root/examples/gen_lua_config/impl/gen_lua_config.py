import logbook
import libs.utils.file_utils as file_utils

from .tt.common import render as tt_render
from .tt.common import set_filter as tt_set_filter
from .excel_sheet_depict import SheetDepict
from .sheet_field_type import SheetFieldType

def lua__field_type_to_string(field_type):
    ret = "unknown"
    if SheetFieldType.is_base_type(field_type):
        for str_val, int_val in SheetFieldType.Base_Type_Strs.items():
            if int_val == field_type:
                ret = str_val
                break
    return ret

def lua__base_field_type_value_to_print(field_val, field_type):
    ret = field_val
    if SheetFieldType.is_base_type(field_type):
        if SheetFieldType.Bool == field_type:
            if field_val:
                ret = "true"
            else:
                ret = "false"
        if SheetFieldType.String == field_type:
            ret = "\"{0}\"".format(str(field_val))
    return ret


tt_set_filter("lua__field_type_to_string", lua__field_type_to_string)
tt_set_filter("lua__base_field_type_value_to_print", lua__base_field_type_value_to_print)

def gen_lua_config(sheet_depict: SheetDepict, out_file):
    ret, content = tt_render("logic_config_values.lua.j2", sheet_depict=sheet_depict)
    # logbook.debug("gen_lua_config {} {}", ret, content)
    if not ret:
        return False
    else:
        file_utils.write_file(out_file, content, encoding='utf-8')