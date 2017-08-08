import os
import sys
import configparser
import codecs
import re
import logging
from config_list import ConfigListDescript 

log = logging

def run(cfg_path):
    if not os.path.exists(cfg_path) or not os.path.isfile(cfg_file):
        log.error(cfg_path + " not exist")
        sys.exit(1)
    env_desc = None
    with codecs.open(cfg_path, "r") as f:
        cfg_praser = configparser.ConfigParser()
        cfg_praser.read_file(f)
        env_desc = ConfigListDescript()
        ret = env_desc.Init(cfg_praser)
        if not ret:
            log.error("EnvDescript Init Fail")
            sys.exit(1) 
            

if __name__ == "__main__":
    log.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        log.debug("")
    cfg_file = sys.argv[1]
    run(os.path.abspath(cfg_file))
