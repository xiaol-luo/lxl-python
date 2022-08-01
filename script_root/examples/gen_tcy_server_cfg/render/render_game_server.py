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



