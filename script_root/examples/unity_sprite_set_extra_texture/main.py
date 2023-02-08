
import argparse
import logbook
import os
import re
import libs.utils.file_utils as file_utils
import typing
from .tt.common import render as tt_render
from libs.common.code_help import IndentFlag as IndentFlag

class ImageData(object):
    main_image : typing.Optional[str]
    main_image_guid: typing.Optional[str]
    extra_image : typing.Optional[str]
    meta_file : typing.Optional[str]
    extra_image_guid: typing.Optional[str]

    def __init__(self):
        super(ImageData, self).__init__()
        self.main_image = None
        self.main_image_guid = None
        self.extra_image = None
        self.meta_file = None
        self.extra_image_guid = None

class UnityFileInfo(object):
    file_path : typing.Optional[str]
    file_guid : typing.Optional[str]

    def __init__(self):
        super(UnityFileInfo, self).__init__()
        self.file_path = None
        self.file_guid = None

class AnimData(object):
    name : str
    image_file_list : typing.List[UnityFileInfo]
    stop_time: float
    image_time_list: typing.List[float]
    file_info: UnityFileInfo
    is_loop: int

    def __init__(self):
        super(AnimData, self).__init__()
        self.name = None
        self.image_file_list = []
        self.image_time_list = [0, 0.083333336, 0.16666667, 0.25, 0.33333334, 0.41666666, 0.5, 0.5833333, 0.6666667, 0.75, 0.8333333, 0.9166667,
                                1, 1.0833334, 1.1666667, 1.25, 1.3333334, 1.416667, 1.5, 1.583334, 1.1666667, 1.75, 1.833334, 1.916667,
                                2, 2.0833334, 0.1666667, 2.25, 0.3333334, 2.416667, 2.5, 0.583334, 2.1666667, 2.75, 0.833334, 2.916667]
        self.stop_time = 0
        self.last_frame_begin_time = 0
        self.file_info = None
        self.is_loop = 1

class AnimControllerData(object):
    name: str
    anim_data_map: typing.Dict[str, AnimData]
    file_info : UnityFileInfo
    


def main(arg_list):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--locate_dir", help="locate_dir")
    arg_parser.add_argument("--main_image_format", help="main_image_format")
    arg_parser.add_argument("--format_image_format", help="format_image_format")
    parse_ret = arg_parser.parse_args(arg_list)

    for (k, v) in vars(parse_ret).items():
        logbook.debug("k, v: {} {}", k, v)

    all_files = file_utils.extract_file_paths(parse_ret.locate_dir)

    re_format_main_image = re.compile("(.*).jpg$")
    re_format_extra_image = re.compile("_(.*).png$")

    image_data_list: typing.List[ImageData] = []
    for main_image in all_files:
        match_main_ret = re_format_main_image.match(os.path.basename(main_image))
        if match_main_ret:
            main_image_dir_path = os.path.dirname(main_image)
            # logbook.debug("reach here")
            for extra_image in all_files:
                if extra_image == main_image:
                    continue
                if os.path.dirname(extra_image) != main_image_dir_path:
                    continue
                match_extra_ret = re_format_extra_image.match(os.path.basename(extra_image))
                if match_extra_ret:
                    if match_extra_ret.group(1) == match_main_ret.group(1):
                        image_data: ImageData = ImageData()
                        image_data_list.append(image_data)
                        image_data.main_image = main_image
                        image_data.extra_image = extra_image
                        image_data.meta_file = "{0}.meta".format(image_data.main_image)
                        image_data.main_image_guid = extract_unity_guid(image_data.meta_file)
                        image_data.extra_image_guid = extract_unity_guid("{0}.meta".format(image_data.extra_image))
                        # logbook.debug("guid {} --- {} === {}", image_data.main_image, image_data.extra_image, image_data.extra_image_guid)
                        break
    for image_data in image_data_list:
        all_lines = file_utils.read_all_lines(image_data.meta_file)
        hit_idx = None
        for idx, line in enumerate(all_lines):
            if line.find("secondaryTextures: []") >= 0:
                hit_idx = idx
                break
        if hit_idx is not None:
            all_lines[hit_idx] =  all_lines[hit_idx].replace(": []", ":")
            all_lines.insert(hit_idx + 1, "    - texture: {fileID: 2800000, guid: " + image_data.extra_image_guid + ", type: 3}\n")
            all_lines.insert(hit_idx + 2, "      name: _MaskTex\n")
            for idx, line in enumerate(all_lines):
                if line.find("internalID: 0") >= 0:
                    all_lines[idx] = line.replace("internalID: 0", "internalID: 1537655665")
            # logbook.debug("-------------------------------- \n{}", all_lines)
            with open(image_data.meta_file, "w") as f:
                f.writelines(all_lines)

    for dir_path, dirs, files in os.walk(parse_ret.locate_dir):
        need_handle = False
        out_dir_falg = "final_product"
        for dir_elem in dirs:
            if "final_product" == dir_elem:
                need_handle = True
        if not need_handle:
            continue
        fish_name = os.path.basename(dir_path)
        anim_ctrl_data = AnimControllerData()
        anim_ctrl_data.name = fish_name
        anim_ctrl_data.anim_data_map = {}
        anim_ctrl_data.file_info = UnityFileInfo()

        out_dir = os.path.join(dir_path, out_dir_falg)
        Fish_Anim_Name_List = ["turn", "idle", "eat", "swim"]
        for anim_name in Fish_Anim_Name_List:
            #anim_name = "turn"
            anim_res_dir = os.path.join(dir_path, anim_name)
            if not os.path.isdir(anim_res_dir):
                continue
            anim_data = AnimData()
            anim_data.is_loop = 1
            if anim_name == "turn":
                anim_data.is_loop = 0
            anim_data.name = anim_name
            anim_ctrl_data.anim_data_map[anim_data.name] = anim_data
            anim_data.file_info = UnityFileInfo()
            anim_data.image_file_list = extract_anim_image_list(image_data_list, anim_res_dir, re_format_main_image, None)
            if len(anim_data.image_file_list) <= 0:
                continue
            anim_data.image_file_list.sort(key=cmp_to_key(sort_cmp_image_file))
            anim_data.stop_time = anim_data.image_time_list[len(anim_data.image_file_list)]
            anim_data.last_frame_begin_time = anim_data.image_time_list[len(anim_data.image_file_list) - 1]
            for elem in anim_data.image_file_list:
                # logbook.debug("------ {}", elem.file_path
                pass
            ret, content = tt_render("anim.meta.j2", fish_name=fish_name, anim_data=anim_data)
            # logbook.debug("gen anim.meta.j2 {} {}", ret, content)
            if not ret:
                pass
            else:
                out_file = os.path.join(out_dir, "{}@{}.anim".format(fish_name, anim_name))
                file_utils.write_file(out_file, content, encoding='utf-8')
                anim_data.file_info.file_path = out_file
                anim_data.file_info.file_guid = extract_unity_guid(out_file + ".meta")
        if not "idle" in anim_ctrl_data.anim_data_map and not "swim" in anim_ctrl_data.anim_data_map:
            logbook.warn("{} has no idle and swim anim", fish_name)
            continue
        else:
            if "idle" in anim_ctrl_data.anim_data_map and "swim" not in anim_ctrl_data.anim_data_map:
                anim_ctrl_data.anim_data_map["swim"] = anim_ctrl_data.anim_data_map["idle"]
            if "swim" in anim_ctrl_data.anim_data_map and "idle" not in anim_ctrl_data.anim_data_map:
                anim_ctrl_data.anim_data_map["idle"] = anim_ctrl_data.anim_data_map["swim"]
        if not "eat" in anim_ctrl_data.anim_data_map:
            anim_ctrl_data.anim_data_map["eat"] = anim_ctrl_data.anim_data_map["swim"]
        all_anim_data_valid = True
        for anim_name in Fish_Anim_Name_List:
            if anim_name not in anim_ctrl_data.anim_data_map:
                logbook.warn("{} has no anim {}", fish_name, anim_name)
                all_anim_data_valid = False
                break
            anim_data = anim_ctrl_data.anim_data_map[anim_name]
            if not anim_data.file_info.file_guid:
                logbook.warn("{} has no anim {}, guid is not ready", fish_name, anim_name)
                all_anim_data_valid = False
                break
        if not all_anim_data_valid:
            continue
        ret, content = tt_render("anim_ctrl.controller.j2", ctrl_data=anim_ctrl_data)
        # logbook.debug("gen anim_ctrl.controller.j2 {} {}", ret, content)
        if not ret:
            pass
        else:
            with IndentFlag():
                out_file = os.path.join(out_dir, "{}.controller".format(fish_name))
                file_utils.write_file(out_file, content, encoding='utf-8')
                anim_ctrl_data.file_info.file_path = out_file
                anim_ctrl_data.file_info.file_guid = extract_unity_guid(out_file + ".meta")
        if anim_ctrl_data.file_info.file_guid:
            sprite_guid = extract_unity_guid(os.path.join(dir_path, "hudimage.png"))
            if not sprite_guid:
                sprite_guid = anim_ctrl_data.anim_data_map["idle"].image_file_list[0].file_guid
            ret, content = tt_render("fish_prefab.prefab.j2", name=fish_name,
                                     ctrl_guid=anim_ctrl_data.file_info.file_guid,
                                     sprite_guid=sprite_guid)
            # logbook.debug("gen anim_ctrl.controller.j2 {} {}", ret, content)
            if not ret:
                pass
            else:
                with IndentFlag():
                    out_file = os.path.join(out_dir, "{}.prefab".format(fish_name))
                    file_utils.write_file(out_file, content, encoding='utf-8')
        else:
            logbook.warn("{} has no controller file or has controller file no meta file", fish_name)



def sort_cmp_image_file(a: UnityFileInfo, b: UnityFileInfo):
    pt_str = ".*\.([0-9]+)\..*"
    a_m = re.match(pt_str, a.file_path)
    b_m = re.match(pt_str, b.file_path)
    a_int = 0
    b_int = 0
    if a_m is not None:
        a_int = int(a_m.group(1))
    if b_m is not None:
        b_int = int(b_m.group(1))
    return  a_int - b_int


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def extract_anim_image_list(all_files: typing.List[ImageData], locate_dir: str,
                            file_pattern: re.Pattern[str], extra_pattern: typing.Optional[re.Pattern[str]]):
    ret_list = []
    for elem in all_files:
        if os.path.dirname(elem.main_image) != locate_dir:
            continue
        if not file_pattern.match(os.path.basename(elem.main_image)):
            continue
        if extra_pattern:
            if not extra_pattern.match(os.path.basename(elem.main_image)):
                continue
        fi = UnityFileInfo()
        ret_list.append(fi)
        fi.file_guid = elem.main_image_guid
        fi.file_path = elem.main_image
        # logbook.debug("fi.file_path {}", fi.file_path)
    return  ret_list


def extract_unity_guid(file_path):
    if not file_path.endswith(".meta"):
        file_path = file_path + ".meta"
    if not os.path.isfile(file_path):
        return  None
    with open(file_path, 'r') as f:
        f.readline()
        line_content = f.readline()
        guid = line_content[6:].strip(" \n")
        return guid



