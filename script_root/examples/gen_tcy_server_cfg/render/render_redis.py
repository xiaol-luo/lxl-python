import tt
import typing
import script_root.libs.utils.file_utils as file_utils
import os
import pathlib

from . import export_file


def export_cluster_start_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_start.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster)
        out_file = export_file.cal_redis_start_file_path(out_root_dir, zone, redis)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_cluster_stop_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_stop.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster)
        out_file = export_file.cal_redis_stop_file_path(out_root_dir, zone, redis)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_cluster_clear_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_clear.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster)
        out_file = export_file.cal_redis_clear_file_path(out_root_dir, zone, redis)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_cluster_logs_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_logs.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster)
        out_file = export_file.cal_redis_logs_file_path(out_root_dir, zone, redis)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_cluster_opera_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster, opera, python_path=None):
    if not python_path:
        python_path = "python"
    else:
        python_path = pathlib.Path(python_path).as_posix()
    script_list = []
    for redis in redis_cluster.server_list.values():
        if "start" == opera:
            script_list.append(export_file.cal_redis_start_file_path(out_root_dir, zone, redis))
        if "stop" == opera:
            script_list.append(export_file.cal_redis_stop_file_path(out_root_dir, zone, redis))
        if "clear" == opera:
            script_list.append(export_file.cal_redis_clear_file_path(out_root_dir, zone, redis))
        if "logs" == opera:
            script_list.append(export_file.cal_redis_logs_file_path(out_root_dir, zone, redis))
    tt_ret, tt_content = tt.render("redis/redis_cluster_opera.py.j2", script_list=script_list, python_path=python_path)
    out_file = export_file.cal_redis_cluster_opera_file_path(out_root_dir, zone, "{0}_cluster.py".format(opera))
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    if tt_ret:
        file_utils.write_file(out_file, tt_content)


def export_cluster_cli_cmds_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster, out_file:str, cmd_list:typing.List[str], is_auth=False):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_cli_cmds.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster, cmd_list=cmd_list, is_auth=is_auth)
        save_file = export_file.cal_redis_cli_cmds_file_path(out_root_dir, zone, out_file)
        os.makedirs(os.path.dirname(save_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(save_file, tt_content)
        # 一个就够了
        break


def export_cluster_setup_cluster_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], redis_cluster):
    for redis in redis_cluster.server_list.values():
        tt_ret, tt_content = tt.render("redis/redis_setup_cluster.py.j2", zone=zone, redis=redis, redis_cluster=redis_cluster)
        save_file = export_file.cal_redis_setup_cluster_file_path(out_root_dir, zone)
        os.makedirs(os.path.dirname(save_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(save_file, tt_content)
        # 一个就够了
        break




