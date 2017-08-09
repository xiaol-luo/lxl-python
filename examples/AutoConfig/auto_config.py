import os
import sys
import configparser
import codecs
import re
import logging
from config_list import ConfigListDescript 
from excel_list import ExcelDescript
import subprocess
import shlex

log = logging

def run(cfg_path):
    cfg_list_desc = ConfigListDescript.load(cfg_path)  
    log.debug(cfg_list_desc)

    for excel2csv_desc in cfg_list_desc.excel2csv_descs:
        excel_desc = ExcelDescript.load(excel2csv_desc.file_path, excel2csv_desc.sheet_name)
        log.debug(excel_desc)

if __name__ == "__main__":
    log.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        log.debug("")
        sys.exit(1)
    cfg_file = sys.argv[1]
    run(os.path.abspath(cfg_file))
