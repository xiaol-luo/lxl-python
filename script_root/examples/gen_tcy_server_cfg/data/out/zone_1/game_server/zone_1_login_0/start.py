# machine Machine
# server_cluster GameServerCluster
# server GameServer
# local_config_file




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
    if exit_when_error and 0 != exit_status:
        print("paramiko_ssh_cmd fail, exit_code is {0}\n out is {1}\n error is {2}".format(exit_status, "".join(out_lines), "".join(error_lines)))
        sys.exit(exit_status)
    return exit_status, "".join(out_lines), "".join(error_lines)


def paramiko_sftp_put(ssh_client: paramiko.SSHClient, local_src:str, remote_dst:str):
    ret = True
    try:
        sftp = ssh_client.open_sftp()
        sftp_attrs = sftp.put(local_src, remote_dst)
        return None != sftp_attrs
    except Exception as e:
        ret = False
        print("paramiko_sftp_put raise exception src:{0}->dst:{1}, error:{2}".format(local_src, remote_dst, e))
    return ret


def paramiko_sftp_get(ssh_client: paramiko.SSHClient, remote_src:str, local_dst:str):
    ret = True
    try:
        sftp = ssh_client.open_sftp()
        sftp.get(remote_src, local_dst)
    except Exception as e:
        ret = False
        print("paramiko_sftp_get raise exception src:{0}->dst:{1}, error:{2}".format(remote_src, local_dst, e))
    return ret

ssh_client = None
with IndentFlag():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="119.91.239.128", port="22", username="root", \
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/xiaol.luo/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="None"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_code,dst=/root/code")
    opt_mount_volumes.append("--mount type=volume,src=tcy_build,dst=/root/build")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/game_server/zone_1_login_0 '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])


paramiko_sftp_put(ssh_client, 'D:/work_space/code/lxl-python/script_root/examples/gen_tcy_server_cfg/data/out/zone_1/game_server/zone_1_login_0/game_config.xml', "/tmp/docker_put_to_data_{0}".format(1))
with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = ""
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/game_server/zone_1_login_0/game_config.xml` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' cp -f /root/tmp/docker_put_to_data_1 /root/zone/zone_1/game_server/zone_1_login_0/game_config.xml  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])


with IndentFlag():
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_code,dst=/root/code")
    opt_mount_volumes.append("--mount type=volume,src=tcy_build,dst=/root/build")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_publish_ports = []
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.20"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {p_ports} {image} {command}".format(
        opt="-d", name="None", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"/root/build/service login /root/zone/zone_1/game_server/zone_1_login_0 /root/zone/zone_1/game_server/zone_1_login_0 /root/zone/zone_1/game_server/zone_1_login_0/game_config.xml /root/code/tanchiyu/server/lua_script --lua_args_begin-- -lua_path /root/code/tanchiyu/server/lua_script . -c_path . -require_files servers.entrance.server_entrance  -execute_fns start_script", p_ports=" ".join(opt_publish_ports)
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)

