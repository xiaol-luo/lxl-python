import tt
import typing
import codes.libs.utils.file_utils as file_utils
import os
import pathlib

from . import export_file


def export_mongodb_start_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongodb in mongo_cluster.mongodb_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongodb/mongodb_start.py.j2", zone=zone, mongodb=mongodb, mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongodb_start_file_path(out_root_dir, zone, mongodb)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_mongodb_stop_file(out_root_dir: str, zone: typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongodb in mongo_cluster.mongodb_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongodb/mongodb_stop.py.j2", zone=zone, mongodb=mongodb,
                                       mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongodb_stop_file_path(out_root_dir, zone, mongodb)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_mongodb_clear_file(out_root_dir: str, zone: typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongodb in mongo_cluster.mongodb_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongodb/mongodb_clear.py.j2", zone=zone, mongodb=mongodb,
                                       mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongodb_clear_file_path(out_root_dir, zone, mongodb)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_mongodb_logs_file(out_root_dir: str, zone: typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongodb in mongo_cluster.mongodb_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongodb/mongodb_logs.py.j2", zone=zone, mongodb=mongodb,
                                       mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongodb_logs_file_path(out_root_dir, zone, mongodb)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)








