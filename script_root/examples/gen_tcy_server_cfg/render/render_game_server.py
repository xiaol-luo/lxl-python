import tt
import typing
import script_root.libs.utils.file_utils as file_utils
import os
import pathlib

from . import export_file


def export_config_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    for server in game_server_cluster.server_list.values():
        tt_ret, tt_content = tt.render("game_server/game_config.xml.j2", zone=zone, server=server)
        if tt_ret:
            out_file = export_file.cal_game_server_config_file_path(out_root_dir, zone, server)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            file_utils.write_file(out_file, tt_content)


def export_start_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    for server in game_server_cluster.server_list.values():
        tt_ret, tt_content = tt.render(
            "game_server/game_server_start.py.j2", zone=zone,
            server_cluster=game_server_cluster, server=server,
            local_config_file= {
                "volume_use": server.config_file,
                "local_path": export_file.cal_game_server_config_file_path(out_root_dir, zone, server),
            },

        )
        if tt_ret:
            out_file = export_file.cal_game_server_start_file_path(out_root_dir, zone, server)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            file_utils.write_file(out_file, tt_content)


def export_stop_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    for server in game_server_cluster.server_list.values():
        tt_ret, tt_content = tt.render("game_server/game_server_stop.py.j2", zone=zone, server=server)
        if tt_ret:
            out_file = export_file.cal_game_server_stop_file_path(out_root_dir, zone, server)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            file_utils.write_file(out_file, tt_content)


def export_logs_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    for server in game_server_cluster.server_list.values():
        tt_ret, tt_content = tt.render("game_server/game_server_logs.py.j2", zone=zone, server=server)
        if tt_ret:
            out_file = export_file.cal_game_server_logs_file_path(out_root_dir, zone, server)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            file_utils.write_file(out_file, tt_content)


def export_clear_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    for server in game_server_cluster.server_list.values():
        tt_ret, tt_content = tt.render("game_server/game_server_clear.py.j2", zone=zone, server=server)
        if tt_ret:
            out_file = export_file.cal_game_server_clear_file_path(out_root_dir, zone, server)
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            file_utils.write_file(out_file, tt_content)


def export_cluster_opera_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster, opera, python_path=None):
    if not python_path:
        python_path = "python"
    else:
        python_path = pathlib.Path(python_path).as_posix()
    script_list = []
    for redis in game_server_cluster.server_list.values():
        if "start" == opera:
            script_list.append(export_file.cal_game_server_start_file_path(out_root_dir, zone, redis))
        if "stop" == opera:
            script_list.append(export_file.cal_game_server_stop_file_path(out_root_dir, zone, redis))
        if "clear" == opera:
            script_list.append(export_file.cal_game_server_clear_file_path(out_root_dir, zone, redis))
        if "logs" == opera:
            script_list.append(export_file.cal_game_server_logs_file_path(out_root_dir, zone, redis))
    tt_ret, tt_content = tt.render("game_server/game_server_cluster_opera.py.j2", script_list=script_list, python_path=python_path)
    out_file = export_file.cal_game_server_cluster_opera_file_path(out_root_dir, zone, "{0}_cluster.py".format(opera))
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    if tt_ret:
        file_utils.write_file(out_file, tt_content)

def get_etcd_setup_game_server_cmds(zone:typing.Dict[str, typing.Dict[str, str]], game_server_cluster):
    ret = []
    ret.append("set {zone_name}/zone_setting/role_min_nums/world_sentinel 1".format(zone_name=zone.name))
    ret.append("set {zone_name}/zone_setting/role_min_nums/gate 1".format(zone_name=zone.name))
    ret.append("set {zone_name}/zone_setting/role_min_nums/game 1".format(zone_name=zone.name))
    ret.append("set {zone_name}/zone_setting/role_min_nums/world 1".format(zone_name=zone.name))
    ret.append("set {zone_name}/zone_setting/role_min_nums/create_role 1".format(zone_name=zone.name))
    ret.append("set {zone_name}/zone_setting/role_min_nums/workbench 1".format(zone_name=zone.name))

    for server in game_server_cluster.server_list.values():
        ret.append("set {zone_name}/zone_setting/allow_join_servers/{server_role}.{server_name} 1".format(
            zone_name=zone.name, server_role=server.server_role, server_name=server.server_name))
        if server.server_role == "world":
            ret.append("set {zone_name}/zone_setting/allow_work_servers/{server_role}.{server_name} 1".format(
                zone_name=zone.name, server_role=server.server_role, server_name=server.server_name))
    return ret

