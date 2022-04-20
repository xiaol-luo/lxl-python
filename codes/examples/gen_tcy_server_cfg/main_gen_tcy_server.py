import argparse
import os.path
import sys
import codecs
import lupa
import logbook
import json
import paramiko
import time
import tt
import typing

logbook.StreamHandler(sys.stdout).push_application()


if __name__ == "__main__":
    logbook.debug("{who} hello", who="nihao")
    logbook.debug("{a[who]} hello", a={"who": "nnn"})
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("in_setting", help="in setting path")
    arg_parse.add_argument("out_setting", help="out setting dir")
    parse_ret = arg_parse.parse_args(sys.argv[1:])
    for (k, v) in vars(parse_ret).items():
        print("k,v {0}, {1}".format(k, v))
    lua_content = None
    with codecs.open(parse_ret.in_setting, "r", encoding="UTF-8") as f:
        f.readline()
        lua_content = f.read()
    if not lua_content:
        sys.exit("-100")
    lua_content = None
    with codecs.open(parse_ret.in_setting, "r", encoding="UTF-8") as f:
        lua_content = f.read()
    lua = lupa.LuaRuntime()
    logbook.debug("--- {}", os.path.dirname(parse_ret.in_setting))
    lua.globals().package.path = str.format("{0};{1}/?.lua", lua.globals().package.path, os.path.dirname(parse_ret.in_setting))
    logbook.debug("lua.execute(lua_content) {}", lua.execute(lua_content))
    lua_g = lua.globals()

    logbook.debug("lua.globals() {}", lua.globals())
    for (k, v) in lua_g.all_setting.items():
        if lupa.lua_type(v) == "table":
            for k2, v2 in v.items():
                logbook.debug("kkk, vvv {} {} {}", k, k2, v2)
        else:
            logbook.debug("kkk, vvv {} {}", k, v)
    tmp = json.loads(lua_g.all_setting_json)
    logbook.debug("lua.globals() {}", json.dumps(tmp, indent=2))

    ll_machine = lua_g.machine_map[lua_g.Machine_Name.ll]
    private_key = paramiko.RSAKey.from_private_key_file(ll_machine.private_key_file, ll_machine.ssh_pwd)
    ssh_client: paramiko.SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ll_machine.ip, port=ll_machine.ssh_port, username=ll_machine.ssh_user, pkey=private_key)

    stdin, stdout, stderr = ssh_client.exec_command("ret=`ls -al`;exit_code=$?;echo bbb $? $exit_code; echo $ret")

    ListOrStr = typing.TypeVar("ListOrStr", typing.List[str], str)

    def execute_ssh_cmd(ssh_client: paramiko.SSHClient, cmd: ListOrStr):
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

    exit_status, out_content, error_content = execute_ssh_cmd(ssh_client, [
        "ls -al",
        r'echo "hello world"',
    ])
    logbook.debug("exit_status" + str(exit_status))
    logbook.debug("out_content" + out_content)
    logbook.debug("error_content" + error_content)

    etcd_cluster = lua_g.all_setting.zone_map.zone_1.etcd_cluster
    etcd = etcd_cluster.server_list[2]
    tt_ret, tt_content = tt.render("etcd/etcd_start.py.j2", machine=ll_machine, etcd=etcd, etcd_cluster=etcd_cluster)
    # logbook.debug("tt ret {} {}", tt_ret, tt_content)

    if tt_ret:
        from codes.libs.utils.file_utils import write_file
        out_file = os.path.join(parse_ret.out_setting, "zone_1/etcd/start.py")
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        write_file(out_file, tt_content)





