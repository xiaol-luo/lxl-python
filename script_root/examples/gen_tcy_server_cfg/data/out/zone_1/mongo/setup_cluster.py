# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_1"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_1/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_1/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.190"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_1", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_1/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_1/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_2"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_2/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_2/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.191"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_2", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_2/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_2/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_3"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_3/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_3/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.192"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_3", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_3/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_3/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_11"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_11/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_11/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.193"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_11", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_11/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_11/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_12"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_12/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_12/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.194"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_12", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_12/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_12/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_13"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_13/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_13/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.195"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_13", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_13/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_13/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_21"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_21/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_21/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.196"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_21", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_21/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_21/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_22"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_22/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_22/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.197"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_22", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_22/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_22/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_23"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_23/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_23/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.198"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_23", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_23/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_23/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_31"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_31/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_31/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.199"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_31", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_31/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_31/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_32"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_32/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_32/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.200"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_32", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_32/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_32/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_33"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_33/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_33/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.201"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_33", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_33/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_33/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongos MongosServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongos_1"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)



with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongos/zone_1_mongos_1/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongos/zone_1_mongos_1/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongos/zone_1_mongos_1/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.189"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongos_1", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongos --bind_ip 0.0.0.0 --port 27017 --logpath /root/zone/zone_1/mongos/zone_1_mongos_1/log.txt --configdb rs_cfg/10.0.1.190:27017,10.0.1.191:27017,10.0.1.192:27017"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# mongo_cluster MongoServerCluster
# zone Zone
# docker_locate_machine Machine
# docker_net DockerNet
# docker_image string
# repl_set_init_cmd_list
# add_shard_cmd_list
# mongos_server




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))



with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.193 --port 27017  --eval 'rs.initiate({ _id:\"rs_db_1\", members:[ {_id:0, host:\"10.0.1.193:27017\"},{_id:1, host:\"10.0.1.194:27017\"},{_id:2, host:\"10.0.1.195:27017\"} ] }); rs.secondaryOk()' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.199 --port 27017  --eval 'rs.initiate({ _id:\"rs_db_3\", members:[ {_id:0, host:\"10.0.1.199:27017\"},{_id:1, host:\"10.0.1.200:27017\"},{_id:2, host:\"10.0.1.201:27017\"} ] }); rs.secondaryOk()' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.190 --port 27017  --eval 'rs.initiate({ _id:\"rs_cfg\", members:[ {_id:0, host:\"10.0.1.190:27017\"},{_id:1, host:\"10.0.1.191:27017\"},{_id:2, host:\"10.0.1.192:27017\"} ] }); rs.secondaryOk()' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.196 --port 27017  --eval 'rs.initiate({ _id:\"rs_db_2\", members:[ {_id:0, host:\"10.0.1.196:27017\"},{_id:1, host:\"10.0.1.197:27017\"},{_id:2, host:\"10.0.1.198:27017\"} ] }); rs.secondaryOk()' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])

import time
time.sleep(15)




    


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.189 --port 27017  --eval 'sh.addShard(\"rs_db_1/10.0.1.193:27017,10.0.1.194:27017,10.0.1.195:27017\")' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.189 --port 27017  --eval 'sh.addShard(\"rs_db_3/10.0.1.199:27017,10.0.1.200:27017,10.0.1.201:27017\")' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.189 --port 27017  --eval 'sh.addShard(\"rs_db_2/10.0.1.196:27017,10.0.1.197:27017,10.0.1.198:27017\")' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.189 --port 27017 admin --eval 'db.createUser({ "user":"root", "pwd":"xiaolzz", "roles":["root"] })' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mongosh --host 10.0.1.189 --port 27017 admin --eval 'db.createUser({ "user":"lxl", "pwd":"xiaolzz", "roles":[ { role: "readWriteAnyDatabase", db: "admin" } ] })' '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    else:
        print("docker exec: run cmd succ, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    # remove docker container
    paramiko_ssh_cmd(ssh_client, [
        "docker container kill {0}".format(ct_name),
        "docker container prune -f",
    ])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_1",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_2",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_3",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_11",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_12",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_13",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_21",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_22",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_23",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_31",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_32",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongodb_33",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongos MongosServer
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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))

paramiko_ssh_cmd(ssh_client, [
    "docker container kill zone_1_mongos_1",
    "docker container prune -f",
])
# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_1"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_1/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_1/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.190"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_1", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_1/id_key_file --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_1/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_1/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_2"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_2/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_2/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.191"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_2", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_2/id_key_file --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_2/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_2/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_3"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_3/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_3/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.192"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_3", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --configsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_3/id_key_file --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_3/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_3/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_11"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_11/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_11/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.193"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_11", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_11/id_key_file --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_11/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_11/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_12"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_12/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_12/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.194"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_12", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_12/id_key_file --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_12/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_12/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_13"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_13/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_13/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.195"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_13", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_13/id_key_file --replSet rs_db_1  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_13/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_13/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_21"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_21/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_21/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.196"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_21", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_21/id_key_file --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_21/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_21/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_22"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_22/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_22/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.197"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_22", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_22/id_key_file --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_22/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_22/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_23"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_23/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_23/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.198"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_23", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_23/id_key_file --replSet rs_db_2  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_23/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_23/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_31"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_31/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_31/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.199"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_31", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_31/id_key_file --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_31/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_31/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_32"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_32/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_32/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.200"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_32", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_32/id_key_file --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_32/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_32/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongodb MongoDbServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongodb_33"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)


with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p /root/zone/zone_1/mongodb/zone_1_mongodb_33/db '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_33/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.201"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongodb_33", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongod --shardsvr --keyFile /root/zone/zone_1/mongodb/zone_1_mongodb_33/id_key_file --replSet rs_db_3  --bind_ip 0.0.0.0 --port 27017 --dbpath /root/zone/zone_1/mongodb/zone_1_mongodb_33/db --logpath /root/zone/zone_1/mongodb/zone_1_mongodb_33/log.txt"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


# machine Machine
# mongo_cluster MongoServerCluster
# mongos MongosServer
# zone Zone
# is_auth




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
        pkey=paramiko.RSAKey.from_private_key_file(r"C:/Users/luoxiaolong/.ssh/keys/root/id_rsa", "xiaolzz"))


with IndentFlag():
    cmds = []
    cmds.append("docker container kill {name}".format(name="zone_1_mongos_1"))
    cmds.append("docker container prune -f")
    paramiko_ssh_cmd(ssh_client, cmds, exit_when_error=False)



with IndentFlag():
    # run docker container
    import random
    ct_name = "ct_{}".format(random.randint(1, 99999999))
    opt_mount_volumes = []
    opt_mount_volumes.append("--mount type=bind,src=/tmp,dst=/root/tmp")
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    run_cmd = "docker run -itd --name {name} {network} {mount_volumes} {image} {command}".format(
        name=ct_name, network=opt_network,  mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian", command="/bin/bash")
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd)
    if 0 != ret:
        print("docker exec: run docker container fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
        sys.exit(ret)
    # execute cmds in docker contianer
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' mkdir -p `dirname /root/zone/zone_1/mongos/zone_1_mongos_1/log.txt` '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' /bin/bash -c 'echo \'seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb\' > /root/zone/zone_1/mongos/zone_1_mongos_1/id_key_file'  '''))
    if 0 != ret:
        print("docker exec: run cmd fail, exit_code is {0}\nstd_out is {1}\nstd_error is {2}\n-------------\n".format(ret, out_txt, error_txt))
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, "docker exec {name} {command}".format(name=ct_name, command=''' chmod 400 /root/zone/zone_1/mongos/zone_1_mongos_1/id_key_file '''))
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
    opt_mount_volumes.append("--mount type=volume,src=tcy_zone,dst=/root/zone")
    opt_network = "--network my-network"
    opt_ip = "--ip 10.0.1.189"
    run_cmd = "docker run {opt} --name {name} {network} {ip} {mount_volumes} {image} {command}".format(
        opt="-d", name="zone_1_mongos_1", network=opt_network, ip=opt_ip, mount_volumes=" ".join(opt_mount_volumes), image="lxl_debian",
        command=r"mongos --bind_ip 0.0.0.0 --port 27017 --keyFile /root/zone/zone_1/mongos/zone_1_mongos_1/id_key_file --logpath /root/zone/zone_1/mongos/zone_1_mongos_1/log.txt --configdb rs_cfg/10.0.1.190:27017,10.0.1.191:27017,10.0.1.192:27017"
    )
    ret, out_txt, error_txt = paramiko_ssh_cmd(ssh_client, run_cmd, exit_when_error=True)
    if 0 != ret:
        print("docker run: run docker container fail, cmd is {0}\n exit_code is {1}\n out is {2}\n error is {3}".format(run_cmd, ret, out_txt, error_txt))
        sys.exit(ret)


