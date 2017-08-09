import os
import sys
import configparser
import re
import logging
from config_list import ConfigListDescript 
from excel_list import ExcelDescript
from csv_generator import CsvGenerator
import subprocess
import shlex

log = logging

def run(cfg_path):
    cfg_list_desc = ConfigListDescript.load(cfg_path)  
    log.debug(cfg_list_desc)

    for excel2csv_desc in cfg_list_desc.excel2csv_descs:
        csv_generator = CsvGenerator(excel2csv_desc)
        if not csv_generator.gen(log):
            log.error("gen csv file %s:%s->%s", 
                excel2csv_desc.file_path, 
                excel2csv_desc.sheet_name, 
                excel2csv_desc.out_csv_file_path)

if __name__ == "__main__":
    log.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        log.debug("")
        sys.exit(1)
    cfg_file = sys.argv[1]
    run(os.path.abspath(cfg_file))
