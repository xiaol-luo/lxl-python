import re

class SheetFieldType(object):
    Min = 0
    Bool = 1
    Int = 2
    Long = 3
    Float = 4
    String = 5
    Raw = 6 # 原封不动地输出,和String的区别只有输出时不带引号。
    Base_Max = 20
    Vec = 21
    Map = 22
    VecVec = 23
    MapVec = 24
    VecMap = 25
    Max = 26

    Base_Type_Strs = {
        "bool": Bool,
        "int": Int,
        "long": Long,
        "float": Float,
        "string": String,
        "raw": Raw,
    }

    @staticmethod
    def is_base_type(field_type):
        return field_type > SheetFieldType.Min and field_type < SheetFieldType.Base_Max

    @staticmethod
    def is_complex_type(field_type):
        return field_type > SheetFieldType.Base_Max and field_type < SheetFieldType.Max

    @staticmethod
    def is_collection_type(field_type):
        return SheetFieldType.is_complex_type(field_type)

    @staticmethod
    def is_vec_collection_type(field_type):
        if SheetFieldType.is_collection_type(field_type):
            return SheetFieldType.Vec == field_type or SheetFieldType.VecVec == field_type

    @staticmethod
    def is_map_collection_type(field_type):
        if SheetFieldType.is_collection_type(field_type):
            return SheetFieldType.Map == field_type or SheetFieldType.MapVec == field_type

    @staticmethod
    def parse_type(type_str):
        ret = False
        field_type = key_type = val_type = SheetFieldType.Min
        type_str = type_str.strip()
        if not ret:  # base
            ret, field_type = SheetFieldType._parse_base_type(type_str)
        if not ret:  # vecvec
            m_ret = re.match(r"^\[\[(.*)\]\]$", type_str)
            if m_ret:
                sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(1))
                if sub_ret and SheetFieldType.is_base_type(sub_type):
                    field_type = SheetFieldType.VecVec
                    val_type = sub_type
                    ret = True
        if not ret:  # mapvec
            m_ret = re.match(r"^<(.*), \[(.*)\]>$", type_str)
            if m_ret:
                parse_succ = False
                sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(1))
                if sub_ret and SheetFieldType.is_base_type(sub_type):
                    field_type = SheetFieldType.MapVec
                    key_type = sub_type
                    sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(2))
                    if sub_ret and SheetFieldType.is_base_type(sub_type):
                        val_type = sub_type
                        parse_succ = True
                        ret = True
                if not parse_succ:
                    field_type = key_type = val_type = SheetFieldType.Min
        if not ret:  # vecmap
            m_ret = re.match(r"^\[<(.*), (.*)>\]$", type_str)
            if m_ret:
                parse_succ = False
                sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(1))
                if sub_ret and SheetFieldType.is_base_type(sub_type):
                    field_type = SheetFieldType.VecMap
                    key_type = sub_type
                    sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(2))
                    if sub_ret and SheetFieldType.is_base_type(sub_type):
                        val_type = sub_type
                        parse_succ = True
                        ret = True
                if not parse_succ:
                    field_type = key_type = val_type = SheetFieldType.Min
        if not ret:  # vec
            m_ret = re.match(r"^\[(.*)\]$", type_str)
            if m_ret:
                sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(1))
                if sub_ret and SheetFieldType.is_base_type(sub_type):
                    field_type = SheetFieldType.Vec
                    val_type = sub_type
                    ret = True
        if not ret:  # map
            m_ret = re.match(r"^<(.*), (.*)>$", type_str)
            if m_ret:
                parse_succ = False
                sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(1))
                if sub_ret and SheetFieldType.is_base_type(sub_type):
                    field_type = SheetFieldType.Map
                    key_type = sub_type
                    sub_ret, sub_type = SheetFieldType._parse_base_type(m_ret.group(2))
                    if sub_ret and SheetFieldType.is_base_type(sub_type):
                        val_type = sub_type
                        parse_succ = True
                        ret = True
                if not parse_succ:
                    field_type = key_type = val_type = SheetFieldType.Min
        return True, field_type, key_type, val_type

    @staticmethod
    def _parse_base_type(type_str):
        if type_str in SheetFieldType.Base_Type_Strs:
            return True, SheetFieldType.Base_Type_Strs[type_str]
        return False, None

    Str_Flag = "\"\"\""

    @staticmethod
    def _extract_base_type_data(data_str, field_type):
        assert(SheetFieldType.is_base_type(field_type))
        ret = None
        if SheetFieldType.Bool == field_type:
            if data_str:
                ret = True
            else:
                ret = False
        if SheetFieldType.Int == field_type:
            if not data_str:
                ret = 0
            else:
                ret = str(int(data_str))
        if SheetFieldType.Float == field_type:
            if not data_str:
                ret = 0.0
            else:
                ret = str(float(data_str))
        if SheetFieldType.String == field_type:
            if not data_str:
                ret = ""
            else:
                ret = str(data_str)
        if SheetFieldType.Raw == field_type:
            ret = str(data_str)
        assert(ret is not None)
        return ret

    @staticmethod
    def extract_data(data_str, field_type, key_type, value_type):
        if SheetFieldType.is_base_type(field_type):
            return SheetFieldType._extract_base_type_data(data_str, field_type)
        start_idx = 0
        Str_Mark_Format = "__Str_Mark_Format__"
        hit_flag_record = []
        str_head_idx = None
        str_tail_idx = None
        if data_str is None:
            data_str = ""
        else:
            data_str = str(data_str)
        while (start_idx < len(data_str)):
            hit_idx = str.find(data_str, SheetFieldType.Str_Flag, start_idx)
            if hit_idx < 0:
                break
            if str_head_idx is None:
                str_head_idx = hit_idx
                start_idx = hit_idx + len(SheetFieldType.Str_Flag)
                continue
            if str_tail_idx is None:
                str_tail_idx = hit_idx + len(SheetFieldType.Str_Flag)
                str_mark = Str_Mark_Format + str(len(hit_flag_record))
                hit_flag_record.append((str_mark, data_str[str_head_idx: str_tail_idx], str_head_idx, str_tail_idx))
                start_idx = str_tail_idx
                str_head_idx = None
                str_tail_idx = None
        if str_head_idx or str_tail_idx:
            print("extract_data: string format is error", data_str)
            return None
        mark_to_str_map = {}
        new_data_str = data_str
        for str_mark, sub_str, str_head_idx, str_tail_idx in reversed(hit_flag_record):
            new_data_str = new_data_str[:str_head_idx] + str_mark + new_data_str[str_tail_idx:]
            mark_to_str_map[str_mark] = sub_str
        if len(new_data_str) <= 0:
            collection_item_list = []
        else:
            collection_item_list = str.split(new_data_str, ";")
        ret = None
        if SheetFieldType.Vec == field_type:
            ret = []
            for item in collection_item_list:
                val = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, item), value_type)
                ret.append(val)
        if SheetFieldType.Map == field_type:
            ret = {}
            for kv_str in collection_item_list:
                kv = str.split(kv_str, ":")
                assert(len(kv) >= 2)
                k = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, kv[0]), key_type)
                v = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, kv[1]), value_type)
                ret[k] = v
        if SheetFieldType.VecVec == field_type:
            ret = []
            for item in collection_item_list:
                sub_ret = []
                ret.append(sub_ret)
                for v_str in str.split(item, "|"):
                    v = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, v_str), value_type)
                    sub_ret.append(v)
        if SheetFieldType.MapVec == field_type:
            ret = {}
            for kv_str in collection_item_list:
                kv = str.split(kv_str, ":")
                assert (len(kv) >= 2)
                k = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, kv[0]), key_type)
                v_list = []
                ret[k] = v_list
                for v_str in str.split(kv[1], "|"):
                    v = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, v_str), value_type)
                    v_list.append(v)
        if SheetFieldType.VecMap == field_type:
            ret = []
            for list_item_str in collection_item_list:
                dt = {}
                ret.append(dt)
                for kv_str in str.split(list_item_str, "|"):
                    kv = str.split(kv_str, ":")
                    assert (len(kv) >= 2)
                    k = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, kv[0]), key_type)
                    v = SheetFieldType._extract_base_type_data(SheetFieldType._recover_data_str(mark_to_str_map, kv[1]), value_type)
                    dt[k] = v
        return ret

    @staticmethod
    def _recover_data_str(mark_map, in_str):
        if in_str not in mark_map:
            return in_str
        out_str = mark_map[in_str]
        return str.replace(out_str, SheetFieldType.Str_Flag, "")









