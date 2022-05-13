import argparse
import os.path
import sys
import codecs
import lupa
import json
import paramiko
import time
import tt
import typing
import render
from codes.libs.common import *

import logbook
logbook.StreamHandler(sys.stdout).push_application()


if __name__ == "__main__":
    logbook.debug("{who} hello", who="nihao")
    logbook.debug("{a[who]} hello", a={"who": "nnn"})
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("in_setting", help="in setting path")
    arg_parse.add_argument("out_setting", help="out setting dir")
    arg_parse.add_argument("--python_path", help="python_path locate path")
    parse_ret = arg_parse.parse_args(sys.argv[1:])
    for (k, v) in vars(parse_ret).items():
        print("k,v {0}, {1}".format(k, v))

    lua = lupa.LuaRuntime()
    lua.globals().package.path = str.format(
        "{0};{1}/?.lua", lua.globals().package.path, os.path.dirname(parse_ret.in_setting))
    with codecs.open(parse_ret.in_setting, "r", encoding="UTF-8") as f:
        logbook.debug("lua.execute(lua_content) {}", lua.execute(f.read()))

    lua_g = lua.globals()
    zone = lua_g.all_setting.zone_map.zone_1
    etcd_cluster = zone.etcd_cluster
    redis_cluster = zone.redis_cluster
    mongo_cluster = zone.mongo_cluster

    tmp = json.loads(lua_g.all_setting_json)
    logbook.debug("lua.globals.all_setting_json {}", json.dumps(tmp, indent=2))

    with IndentFlag():
        # etcd
        render.render_etcd.export_cluster_start_file(parse_ret.out_setting, zone, etcd_cluster)
        render.render_etcd.export_cluster_stop_file(parse_ret.out_setting, zone, etcd_cluster)
        render.render_etcd.export_cluster_clear_file(parse_ret.out_setting, zone, etcd_cluster)
        render.render_etcd.export_cluster_logs_file(parse_ret.out_setting, zone, etcd_cluster)
        render.render_etcd.export_cluster_opera_file(parse_ret.out_setting, zone, etcd_cluster, "start", parse_ret.python_path)
        render.render_etcd.export_cluster_opera_file(parse_ret.out_setting, zone, etcd_cluster, "stop", parse_ret.python_path)
        render.render_etcd.export_cluster_opera_file(parse_ret.out_setting, zone, etcd_cluster, "clear", parse_ret.python_path)
        render.render_etcd.export_cluster_opera_file(parse_ret.out_setting, zone, etcd_cluster, "logs", parse_ret.python_path)
        render.render_etcd.export_cluster_etcdctl_cmds_file(parse_ret.out_setting, zone, etcd_cluster,  "etcdctl_test.py", ["ls /"], is_auth=True)
        render.render_etcd.export_cluster_enable_auth_file(parse_ret.out_setting, zone, etcd_cluster)

    with IndentFlag():
        # redis
        render.render_redis.export_cluster_start_file(parse_ret.out_setting, zone, redis_cluster)
        render.render_redis.export_cluster_stop_file(parse_ret.out_setting, zone, redis_cluster)
        render.render_redis.export_cluster_clear_file(parse_ret.out_setting, zone, redis_cluster)
        render.render_redis.export_cluster_logs_file(parse_ret.out_setting, zone, redis_cluster)
        render.render_redis.export_cluster_opera_file(parse_ret.out_setting, zone, redis_cluster, "start", parse_ret.python_path)
        render.render_redis.export_cluster_opera_file(parse_ret.out_setting, zone, redis_cluster, "stop", parse_ret.python_path)
        render.render_redis.export_cluster_opera_file(parse_ret.out_setting, zone, redis_cluster, "clear", parse_ret.python_path)
        render.render_redis.export_cluster_opera_file(parse_ret.out_setting, zone, redis_cluster, "logs", parse_ret.python_path)
        render.render_redis.export_cluster_setup_cluster_file(parse_ret.out_setting, zone, redis_cluster)
        render.render_redis.export_cluster_cli_cmds_file(parse_ret.out_setting, zone, redis_cluster, "cli_test.py", ["set a 0", "get a"], is_auth=True)

    with IndentFlag():
        render.render_mongo.export_mongodb_start_file(parse_ret.out_setting, zone, mongo_cluster)
        render.render_mongo.export_mongodb_stop_file(parse_ret.out_setting, zone, mongo_cluster)
        render.render_mongo.export_mongodb_clear_file(parse_ret.out_setting, zone, mongo_cluster)
        render.render_mongo.export_mongodb_logs_file(parse_ret.out_setting, zone, mongo_cluster)




