import os.path


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


def filter_dirname(in_path):
    return os.path.dirname(in_path)

def setup_filters(set_filter_fn):
    set_filter_fn("dirname", filter_dirname)