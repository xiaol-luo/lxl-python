import chardet

def convert_to_utf8(in_param):
    ret = in_param
    in_t = type(in_param)
    if in_t == str or in_t == bytes:
        if in_t == bytes:
            dt = chardet.detect(in_param)
            u_str = str.encode(in_param, dt.encoding)
            ret = str.encode(u_str, "utf-8")
    return  ret