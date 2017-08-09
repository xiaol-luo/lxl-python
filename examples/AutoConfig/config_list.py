import configparser
import re
import os
import codecs

STRING_EMPTY = ""

class Excel2CsvDescript(object):
    def __init__(self, owner, **kwargs):
        self._owner = owner
        self.file_path = STRING_EMPTY
        self.sheet_name = STRING_EMPTY
        self.out_csv_file_path = STRING_EMPTY
        self.class_name = STRING_EMPTY
        self.out_cs_file_path = STRING_EMPTY
        self.out_cpp_file_path = STRING_EMPTY
        self.out_lua_file_path = STRING_EMPTY
        return super().__init__(**kwargs)
    
    def Init(self, cfg_section):
        self.file_path = cfg_section["file_path"]
        self.sheet_name = cfg_section["sheet_name"]
        self.out_csv_file_path = cfg_section["out_csv_file_path"]
        self.class_name = cfg_section["class_name"]
        self.out_cs_file_path = cfg_section["out_cs_file_path"]
        self.out_cpp_file_path = cfg_section["out_cpp_file_path"]
        self.out_lua_file_path = cfg_section["out_lua_file_path"]
        return True


class ConfigListDescript(object):
    ENV_SECTION = "env"
    EXCEL2CSV_REGEX_PATTERN = r'^excel2csv-.*'

    def __init__(self, **kwargs):
        self.excel_dir = STRING_EMPTY
        self.out_config_dir = STRING_EMPTY
        self.out_code_dir = STRING_EMPTY
        self.excel2csv_descs = []
        return super().__init__(**kwargs)

    def Init(self, cfg_praser):
        for section in cfg_praser.sections():
            print("{0}".format(section))
        if not cfg_praser.has_section(ConfigListDescript.ENV_SECTION):
            return False
        env_section = cfg_praser[ConfigListDescript.ENV_SECTION]
        self.excel_dir = env_section["excel_dir"]
        self.out_config_dir = env_section["out_config_dir"]
        self.out_code_dir = env_section["out_code_dir"]
        self.excel2csv_descs = []
        for section_name in cfg_praser.sections():
            if not re.match(ConfigListDescript.EXCEL2CSV_REGEX_PATTERN, section_name):
                continue
            excel2csv_desc = Excel2CsvDescript(self)
            if not excel2csv_desc.Init(cfg_praser[section_name]):
                log.error("cfg_path - {0} {1} error {2}".format(cfg_path, section_name, cfg_praser.sections[section_name]))
            else:
                self.excel2csv_descs.append(excel2csv_desc)
        return True

    @staticmethod
    def load(file_path):
        env_desc = None
        if os.path.exists(file_path) and os.path.isfile(file_path): 
            with codecs.open(file_path, "r") as f:
                cfg_praser = configparser.ConfigParser()
                cfg_praser.read_file(f)
                env_desc = ConfigListDescript()
                if not env_desc.Init(cfg_praser):
                    env_desc = None
        return env_desc