from lpy_define import *
import pickle
import logging
import sys
from sol_luabind import GenLuaBindCode

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging

if __name__ == "__main__":
    lpy_ret = None
    with open("yacc_ret.txt", 'rb') as f:
        lpy_ret = pickle.load(f)
    if not lpy_ret:
        log.error("pickle.load fail")
        sys.exit(-1)
    ret = GenLuaBindCode(lpy_ret)
