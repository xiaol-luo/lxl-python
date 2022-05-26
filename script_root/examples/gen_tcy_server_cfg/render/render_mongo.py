import tt
import typing
import script_root.libs.utils.file_utils as file_utils
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


def export_mongos_start_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongos in mongo_cluster.mongos_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongos/mongos_start.py.j2", zone=zone, mongos=mongos, mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongos_start_file_path(out_root_dir, zone, mongos)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_mongos_stop_file(out_root_dir: str, zone: typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongos in mongo_cluster.mongos_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongos/mongos_stop.py.j2", zone=zone, mongos=mongos,
                                       mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongos_stop_file_path(out_root_dir, zone, mongos)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_mongos_logs_file(out_root_dir: str, zone: typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    for mongos in mongo_cluster.mongos_server_list.values():
        tt_ret, tt_content = tt.render("mongo/mongos/mongos_logs.py.j2", zone=zone, mongos=mongos,
                                       mongo_cluster=mongo_cluster)
        out_file = export_file.cal_mongos_logs_file_path(out_root_dir, zone, mongos)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        if tt_ret:
            file_utils.write_file(out_file, tt_content)


def export_setup_cluster_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], mongo_cluster):
    docker_locate_machine = mongo_cluster.mongodb_server_list[1].locate_machine
    docker_net = mongo_cluster.mongodb_server_list[1].docker_ip.docker_net
    docker_image = mongo_cluster.mongodb_server_list[1].image
    mongos_server = mongo_cluster.mongos_server_list[1]
    repl_set_init_cmd_list = []
    add_shard_cmd_list = []
    for repl_set in mongo_cluster.fo_repl_set_map.values():
        member_list = []
        for i, svr in enumerate(repl_set.server_list.values()):
            member_list.append('{{_id:{0}, host:\\"{1}:{2}\\"}}'.format(i, svr.docker_ip.fo_ip, svr.client_port))
        rs_init_cmd = 'rs.initiate({{ _id:\\"{0}\\", members:[ {1} ] }}); rs.secondaryOk()'.format(repl_set.name, ",".join(member_list))
        add_shard_cmd = 'sh.addShard(\\"{0}/{1}\\")'.format(repl_set.name, repl_set.fo_host_list_str)
        db = ""
        server = repl_set.server_list[1]
        repl_set_init_cmd_list.append({
            "db": db,
            "cmd": rs_init_cmd,
            "server": server,
        })
        if repl_set.repl_set_role == "shardsvr":
            add_shard_cmd_list.append({
                "db": db,
                "cmd": add_shard_cmd,
                "server": mongos_server,
            })
    tt_ret, tt_content = tt.render(
        "mongo/mongo_cli/mongo_cli_setup_cluster.py.j2",
        zone=zone, mongo_cluster=mongo_cluster, docker_locate_machine=docker_locate_machine,
        docker_net=docker_net, docker_image=docker_image,
        repl_set_init_cmd_list=repl_set_init_cmd_list, add_shard_cmd_list=add_shard_cmd_list
    )
    out_file = export_file.cal_mongo_setup_cluster_file_path(out_root_dir, zone)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    if tt_ret:
        file_utils.write_file(out_file, tt_content)


def export_cli_cmds_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], mongo_cluster, out_file:str, cmd_db, cmd_list:typing.List[str], is_auth=False):
    pass
