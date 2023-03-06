from gevent import monkey; monkey.patch_all()
import sys
import argparse
from libs.common.code_help import IndentFlag
import typing

if typing.TYPE_CHECKING:
    class TH_Arg(object):
        robot_key: str
        robot_secret: str
        http_proxy: str
        robot_send_url: str

def main(arg_list):
    arg_parser: argparse.ArgumentParser = argparse.ArgumentParser()
    arg_parser.add_argument("--robot_key", help="robot_key")
    arg_parser.add_argument("--robot_secret", help="robot_secret")
    arg_parser.add_argument("--robot_send_url", help="robot_send_url")
    parse_ret:TH_Arg = arg_parser.parse_args(arg_list)

    from .dd_robot_client.dd_robot_client import DDRobotClient
    robot_client = DDRobotClient(parse_ret.robot_key, parse_ret.robot_secret, parse_ret.robot_send_url)
    # init_ret = robot_client.fetch_token()
    # if not init_ret:
    #    sys.exit(-1)
    # robot_client.send_text("nt hello robot!")
    from .web_app import WebIns
    from .app_dd import AppDD
    from .bottle import Bottle
    bt = Bottle()
    g_ins = WebIns(bt)
    g_ins.set_app(AppDD(g_ins, parse_ret.robot_secret, robot_client))
    g_ins.run(host='0.0.0.0', port=8080, debug=True, reloader=True)

