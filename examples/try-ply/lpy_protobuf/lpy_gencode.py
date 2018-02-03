from lpy_define import *
import pickle
import logging
import sys

from sol_luabind import GenLuaBindCode

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging

if __name__ == "__main__":
    lpy_ret = None
    yacc_ret_file = "yacc_ret.txt"
    if len(sys.argv) >= 2:
        yacc_ret_file = sys.argv[1]
    out_dir = STR_EMPTY
    if len(sys.argv) >= 3:
        out_dir = sys.argv[2]
    with open(yacc_ret_file, 'rb') as f:
        lpy_ret = pickle.load(f)
    if not lpy_ret:
        log.error("pickle.load fail")
        sys.exit(-1)
    ret = GenLuaBindCode(lpy_ret, out_dir)
