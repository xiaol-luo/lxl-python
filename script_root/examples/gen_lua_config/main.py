import argparse
import os

import logbook

from .impl.setting_parser import SettingParser
from .impl.excel_sheet_depict import SheetDepict, parse_sheet_depict
from .impl.gen_lua_config import gen_lua_config

def main(arg_list):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--setting_file", help="setting file path")
    parse_ret = arg_parser.parse_args(arg_list)

    for (k, v) in vars(parse_ret).items():
        logbook.debug("k, v: {} {}", k, v)

    logbook.debug("working dir {}", os.getcwd())

    setting_parser = SettingParser()
    setting_parser.parse_file(parse_ret.setting_file)

    for item in setting_parser.output_list:
        sheet_depict = parse_sheet_depict(item.excel_path, item.sheet_name)
        if sheet_depict:
            gen_lua_config(sheet_depict, item.out_lua_file)
        else:
            logbook.error("parse_sheet_depict fail, {} {}", item.excel_path, item.sheet_name)
