# machine Machine
# redis_cluster RedisServerCluster
# redis RedisServer
# zone Zone




import paramiko
import typing
import random
import sys
import os

class IndentFlag(object):
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass


ListOrStr = typing.TypeVar("ListOrStr", typing.List[str], str)


def paramiko_ssh_cmd(ssh_client: paramiko.SSHClient, cmd: ListOrStr, exit_when_error:bool=False):
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
    if exit_when_error:
        print("paramiko_ssh_cmd fail, exit_code is {0}\n out is {1}\n error is {2}".format(exit_status, "".join(out_lines), "".join(error_lines)))
        sys.exit(exit_status)
    return exit_status, "".join(out_lines), "".join(error_lines)


ssh_client = None
with IndentFlag():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="119.91.239.128", port="22", username="root", \
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_redis_2"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = ""
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command="rm -rf /root/zone/zone_1/redis/zone_1_redis_2"))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])