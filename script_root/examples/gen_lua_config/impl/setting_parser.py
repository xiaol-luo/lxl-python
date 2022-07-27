import ctypes
import typing
import xml.etree.ElementTree as ET
import os

import logbook


class SettingEnv(object):
    excel_dir: str
    out_lua_dir: str

    def __init__(self):
        excel_dir = None
        out_lua_dir = None

class SettingOutput(object):
    excel_path: str
    sheet_name: str
    out_lua_file: str

    def __init__(self):
        excel_path = None
        sheet_name = None
        out_lua_file = None

class SettingParser(object):
    env: SettingEnv
    output_list: typing.List[SettingOutput]

    def __init__(self):
        self.env = None
        self.output_list = None
    pass

    def parse_file(self, file_path):
        xml: ET = ET.parse(file_path)
        xml_root: ET.Element = xml.getroot()
        self.env = SettingEnv()
        self.env.excel_dir = xml_root.find("env/excel_dir").text
        self.env.out_lua_dir = xml_root.find("env/out_lua_dir").text
        self.output_list = []
        for item in xml_root.findall("output_list/output"):
            output = SettingOutput()
            self.output_list.append(output)
            output.excel_path = os.path.join(self.env.excel_dir, item.get("excel_path"))
            output.sheet_name = item.get("sheet_name")
            output.out_lua_file = os.path.join(self.env.out_lua_dir, item.get("out_lua_file"))
            logbook.debug("item {} {} {}", output.excel_path, output.sheet_name, output.out_lua_file)




