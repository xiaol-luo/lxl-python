import argparse
import os.path
import sys
import codecs
import lupa
import logbook
import json
import paramiko
import time

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
    '''
    logbook.debug("lua.globals() {}", lua.globals())
    for (k, v) in lua_g.all_setting.items():
        if lupa.lua_type(v) == "table":
            for k2, v2 in v.items():
                logbook.debug("kkk, vvv {} {} {}", k, k2, v2)
        else:
            logbook.debug("kkk, vvv {} {}", k, v)
    tmp = json.loads(lua_g.all_setting_json)
    logbook.debug("lua.globals() {}", json.dumps(tmp, indent=2))
    '''
    ll_machine = lua_g.machine_map[lua_g.Machine_Name.ll]
    private_key = paramiko.RSAKey.from_private_key_file(ll_machine.private_key_file, ll_machine.ssh_pwd)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ll_machine.ip, port=ll_machine.ssh_port, username=ll_machine.ssh_user, pkey=private_key)
    stdin, stdout, stderr = ssh_client.exec_command("ret=`ls -al`;exit_code=$?;echo bbb $? $exit_code; echo $ret")
    logbook.debug("----------------------")
    chan = ssh_client.invoke_shell()
    stdout = chan.recv(9999)
    # chan.send("cd /root;")
    chan.sendall("ls -al\n")
    chan.sendall("ret=$?\n")
    chan.sendall("echo xxx $? $ret\n")
    chan.sendall("exit $ret\n")
    chan.shutdown_write()


    exit_code = chan.recv_exit_status()
    while chan.recv_ready():
        stdout = chan.recv(1024)
        logbook.debug(stdout.decode("utf-8"))
        logbook.debug("\n")
    logbook.debug("exit code is {}", exit_code)
    sys.exit(2)


