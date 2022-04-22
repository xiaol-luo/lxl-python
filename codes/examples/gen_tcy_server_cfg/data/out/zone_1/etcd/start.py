# machine Machine
# etcd_cluster EtcdServerCluster
# etcd EtcdServer

import paramiko
import typing
import random
import sys
import os

class IndentHelp(object):
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass


ListOrStr = typing.TypeVar("ListOrStr", typing.List[str], str)


def paramiko_ssh_cmd(ssh_client: paramiko.SSHClient, cmd: ListOrStr):
    shell: paramiko.Channel = ssh_client.invoke_shell()
    if isinstance(cmd, str):
        shell.sendall(cmd + "\n")
    else:
        for e in cmd:
            shell.sendall(e + "\n")
    shell.sendall("exit $?\n")
    exit_status = shell.recv_exit_status()
    out_lines = []
    while True:
        recv_data = shell.recv(1024)
        if len(recv_data) > 0:
            out_lines.append(recv_data.decode("utf-8"))
        else:
            break
    error_lines = []
    while True:
        recv_data = shell.recv_stderr(1024)
        if len(recv_data) > 0:
            error_lines.append(recv_data.decode("utf-8"))
        else:
            break
    return exit_status, "".join(out_lines), "".join(error_lines)



ssh_client = None
with IndentHelp():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="119.91.239.128", port="22", username="root", \
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


# docker run -d --network my-network --name zone_1_etcd_2 --mount type=volume,src=tcy_code,dst=/root/code --mount type=volume,src=tcy_build,dst=/root/build --mount type=volume,src=tcy_zone,dst=/root/zone --mount type=bind,src=/root/tmp,dst=/root/tmp  lxl_debian etcd

with IndentHelp():
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.181"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="", name="zone_1_etcd_2", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="etcd")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret or True:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


with IndentHelp():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command="mkdir -p /root/zone/zone_1/etcd/zone_1_etcd_2"))
    if 0 != ret:
        print("docker exec: run cmd fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format("mkdir -p /root/zone/zone_1/etcd/zone_1_etcd_2", ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])


# docker run --name zone_1_etcd_2 --network my-network \
#    --ip 10.0.1.181 --mount type=volume,src=tcy_zone,dst=/root/zone \
#    lxl_debian ls -al