import os
import sys
import configparser
import codecs
import re
import logging
from config_list import ConfigListDescript 

log = logging

def run(cfg_path):
    env_desc = ConfigListDescript.load(cfg_path)
        

if __name__ == "__main__":
    log.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        log.debug("")
    cfg_file = sys.argv[1]
    run(os.path.abspath(cfg_file))
