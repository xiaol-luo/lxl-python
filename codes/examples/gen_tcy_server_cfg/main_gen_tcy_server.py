import argparse
import os.path
import sys
import codecs
from slpp import slpp
import lupa
import logbook
logbook.StreamHandler(sys.stdout).push_application()

if __name__ == "__main__":
    logbook.debug("{who} hello", who="nihao")
    logbook.debug("{a[who]} hello", a={"who": "nnn"})
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("in_setting", help="in setting path")
    arg_parse.add_argument("out_setting", help="out setting dir")
    parse_ret = arg_parse.parse_args(sys.argv[1:])
    for (k, v) in vars(parse_ret).items():
        print("k,v {0}, {1}".format(k, v))
    lua_content = None
    with codecs.open(parse_ret.in_setting, "r", encoding="UTF-8") as f:
        f.readline()
        lua_content = f.read()
    if not lua_content:
        sys.exit("-100")
    all_zone_settings = slpp.decode(lua_content)
    logbook.debug("all_zone_setting {} {} {}", type(all_zone_settings), all_zone_settings, lua_content)
    lua_content = None
    with codecs.open(parse_ret.in_setting, "r", encoding="UTF-8") as f:
        lua_content = f.read()
    lua = lupa.LuaRuntime()
    logbook.debug("--- {}", os.path.dirname(parse_ret.in_setting))
    lua.globals().package.path = str.format("{0};{1}/?.lua", lua.globals().package.path, os.path.dirname(parse_ret.in_setting))
    logbook.debug("lua.execute(lua_content) {}", lua.execute(lua_content))
    lua_g = lua.globals()
    logbook.debug("lua.globals() {}", lua.globals())
    logbook.debug("lua.globals() {}", lua_g.all_setting)
    for (k, v) in lua_g.all_setting.items():
        if lupa.lua_type(v) == "table":
            for k2, v2 in v.items():
                logbook.debug("kkk, vvv {} {} {}", k, k2, v2)
        else:
            logbook.debug("kkk, vvv {} {}", k, v)



