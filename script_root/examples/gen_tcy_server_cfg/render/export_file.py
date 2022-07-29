import os
import pathlib


def path_batch_join(p1, p2, *args):
    ret = os.path.join(p1, p2)
    for e in args:
        ret = os.path.join(ret, e)
    return pathlib.Path(ret).as_posix()


def cal_etcd_start_file_path(root_dir, zone, etcd):
    return path_batch_join(root_dir, zone.name, "etcd", etcd.name, "start.py")


def cal_etcd_stop_file_path(root_dir, zone, etcd):
    return path_batch_join(root_dir, zone.name, "etcd", etcd.name, "stop.py")


def cal_etcd_clear_file_path(root_dir, zone, etcd):
    return path_batch_join(root_dir, zone.name, "etcd", etcd.name, "clear.py")


def cal_etcd_logs_file_path(root_dir, zone, etcd):
    return path_batch_join(root_dir, zone.name, "etcd", etcd.name, "logs.py")


def cal_etcd_etcdctl_cmds_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "etcd", out_file)


def cal_etcd_enable_auth_file_path(root_dir, zone):
    return path_batch_join(root_dir, zone.name, "etcd", "enable_auth.py")


def cal_etcd_cluster_opera_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "etcd", out_file)


def cal_redis_start_file_path(root_dir, zone, redis):
    return path_batch_join(root_dir, zone.name, "redis", redis.name, "start.py")


def cal_redis_stop_file_path(root_dir, zone, redis):
    return path_batch_join(root_dir, zone.name, "redis", redis.name, "stop.py")


def cal_redis_clear_file_path(root_dir, zone, redis):
    return path_batch_join(root_dir, zone.name, "redis", redis.name, "clear.py")


def cal_redis_logs_file_path(root_dir, zone, redis):
    return path_batch_join(root_dir, zone.name, "redis", redis.name, "logs.py")


def cal_redis_cluster_opera_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "redis", out_file)


def cal_redis_setup_cluster_file_path(root_dir, zone):
    return path_batch_join(root_dir, zone.name, "redis", "setup_cluster.py")


def cal_redis_cli_cmds_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "redis", out_file)


def cal_mongodb_start_file_path(root_dir, zone, mongodb):
    return path_batch_join(root_dir, zone.name, "mongo", "mongodb", mongodb.name, "start.py")


def cal_mongodb_stop_file_path(root_dir, zone, mongodb):
    return path_batch_join(root_dir, zone.name, "mongo", "mongodb", mongodb.name, "stop.py")


def cal_mongodb_clear_file_path(root_dir, zone, mongodb):
    return path_batch_join(root_dir, zone.name, "mongo", "mongodb", mongodb.name, "clear.py")


def cal_mongodb_logs_file_path(root_dir, zone, mongodb):
    return path_batch_join(root_dir, zone.name, "mongo", "mongodb", mongodb.name, "logs.py")


def cal_mongos_start_file_path(root_dir, zone, mongos):
    return path_batch_join(root_dir, zone.name, "mongo", "mongos", mongos.name, "start.py")


def cal_mongos_stop_file_path(root_dir, zone, mongos):
    return path_batch_join(root_dir, zone.name, "mongo", "mongos", mongos.name, "stop.py")


def cal_mongos_logs_file_path(root_dir, zone, mongos):
    return path_batch_join(root_dir, zone.name, "mongo", "mongos", mongos.name, "logs.py")


def cal_mongos_clear_file_path(root_dir, zone, mongos):
    return path_batch_join(root_dir, zone.name, "mongo", "mongos", mongos.name, "clear.py")


def cal_mongo_cluster_opera_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "mongo", out_file)


def cal_mongo_setup_cluster_file_path(root_dir, zone):
    return path_batch_join(root_dir, zone.name, "mongo", "setup_cluster.py")


def cal_test_file_path(root_dir, zone):
    return path_batch_join(root_dir, zone.name, "test.py")


def cal_game_server_config_file_path(root_dir, zone, server):
    return path_batch_join(root_dir, zone.name, "game_server", server.server_name, "game_config.xml")


def cal_game_server_start_file_path(root_dir, zone, server):
    return path_batch_join(root_dir, zone.name, "game_server", server.server_name, "start.py")


