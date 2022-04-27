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


def cal_etcd_etcdctl_opera_file_path(root_dir, zone, out_file):
    return path_batch_join(root_dir, zone.name, "etcd", out_file)


