# machine Machine
# etcd_cluster EtcdServerCluster
# etcd EtcdServer

import paramiko
import typing
import random

class IndentHelp(object):
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass


ListOrStr = typing.TypeVar("ListOrStr", typing.List[str], str)


def paramiko_ssh_cmd(ssh_client: paramiko.SSHClient, cmd: ListOrStr):
    shell: paramiko.Channel = ssh_client.invoke_shell()
    if cmd is str:
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

with IndentHelp():
    cmds = []
    with IndentHelp():
        ct_name = "ct_{}".format(random.randint(1, 99999999))
        mount_volumes = []
        cmds.append("docker run {opt} --name {name} --network {network} { mount_volumes } {image} {command}".format(
            opt="-itd", name=ct_name, network="my-network",  mount_volumes ="".join(mount_volumes), image="lxl_debian", command="/bin/bash"))
        print("cmds", cmds)
# docker run -d --network my-network --name tcy --mount type=volume,src=tcy_code,dst=/root/code --mount type=volume,src=tcy_build,dst=/root/build --mount type=volume,src=tcy_zone,dst=/root/zone --mount type=bind,src=/root/tmp,dst=/root/tmp  lxl_debian etcd
# docker exec etcd_2 /bin/bash -c "ps -ef | grep etc | grep -v grep"


# docker run -d --network my-network --name zone_1_etcd_2 --mount type=volume,src=tcy_code,dst=/root/code --mount type=volume,src=tcy_build,dst=/root/build --mount type=volume,src=tcy_zone,dst=/root/zone --mount type=bind,src=/root/tmp,dst=/root/tmp  lxl_debian etcd

with IndentHelp():
    print("hello world")

shell.sendall("ls -al\n")
shell.sendall("ret=$?\n")
shell.sendall("echo xxx $? $ret\n")
shell.sendall("exit $ret\n")
shell.shutdown_write()