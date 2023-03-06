import json
import shlex
import typing
import time

from ..web_app import WebApp, WebIns
import gevent
import gevent.subprocess
import logbook
from ..bottle import FormsDict
from libs.gevent_ext.gevent_cmd import GeventCmd
import enum
from .app_setting import get_setting
from ..dd_robot_client.dd_robot_client import DDRobotClient


def _print_dict(dt: FormsDict, tag=""):
    if dt is None:
        logbook.debug("{} is none", tag)
    else:
        for k, v in dt.items():
            logbook.debug("{} k:v={}:{}", tag, k, v)


class DD_Cmd(enum.Enum):
    Build_Tcy_Android = "Build_Tcy_Android"
    Build_Tcy_Ios = "Build_Tcy_Ios"


class AppDD(WebApp):
    web_ins: WebIns
    app_secret: str
    _cmd_map: typing.Dict[str, GeventCmd]
    robot_client: DDRobotClient

    def __init__(self, web_ins: WebIns, app_secret, robot_client: DDRobotClient):
        super(AppDD, self).__init__(web_ins)
        self._last_uuid = 0
        self.app_secret = app_secret
        self._cmd_dt = {}
        self._setting = get_setting()
        self.robot_client = robot_client
        logbook.debug("_setting {}", self._setting)

    @staticmethod
    def make_simple_result(self, error_num, error_msg):
        if error_msg is None:
            error_msg = ""
        return '{"error_num": {}, "error_msg":{}}'.format(error_num, error_msg)

    def next_uuid(self):
        self._last_uuid = self._last_uuid + 1
        return self._last_uuid

    def dd_sign_str(self, in_str: str):
        ret = self.dd_sign_bytes(in_str.encode('utf-8'))
        return ret

    def dd_sign_bytes(self, in_bin):
        import hmac
        import base64
        import hashlib
        mac_obj = hmac.new(self.app_secret.encode('utf-8'), in_bin, digestmod=hashlib.sha256)
        sign = base64.b64encode(mac_obj.digest()).decode('utf-8')
        return sign

    def dd_cmd(self):
        # descript https://open.dingtalk.com/document/orgapp/receive-message
        head_dt: FormsDict = self.web_ins.request.headers
        arg_dt: typing.Dict = self.web_ins.request.json
        # _print_dict(head_dt, "head_dt")
        # _print_dict(arg_dt, "arg_dt")
        if self.web_ins.request.method == "POST":
            arg_timestamp = head_dt.get("Timestamp", 0)  # 这个是毫秒
            now_timestamp = int(time.time() * 1000)
            if abs(now_timestamp - int(arg_timestamp)) >= 3600 * 1000:
                return  AppDD.make_simple_result(100, "timestamp invalid")
            sign = self.dd_sign_str(str(arg_timestamp) + "\n" + self.app_secret)
            if sign != head_dt.get("Sign", None):
                return AppDD.make_simple_result(110, "sign not equal")

        uuid = self.next_uuid()
        # subprocess和gevent配合使用看这些
        # https://stackoverflow.com/questions/19497587/get-live-stdout-from-gevent-subprocess
        # https://gist.github.com/zhangchunlin/05576572b628f5bf9d74

        def print_line(p, line):
            logbook.debug("uuid:{} line {}",uuid, line)

        def handle_done(p:GeventCmd):
            logbook.debug("cmd is done {} {}", p.cmd, p.return_code)

        from .app_dd_task import AppDDTask_BuildAndroid
        app_setting = get_setting()
        task = AppDDTask_BuildAndroid(app_setting, self.robot_client)
        task.start()
        gevent.joinall([task])

        '''
        logbook.debug("start cmd")
        cmd = GeventCmd("ping -n 15 www.baidu.com", handle_done=handle_done,  handle_stdout_content=print_line,
                        handle_stderr_content=print_line, capture_output=True)
        cmd.execute()
        '''
        return "dd_cmd done"

    def hello(self):
        query_dict: FormsDict = self.web_ins.request.params
        _print_dict(query_dict, "web_params")
        is_skip: int = query_dict.get("skip", 0)
        uid = self.next_uuid()
        logbook.debug("hello {} {} {} {}", uid, self.web_ins.request.method, is_skip, type(is_skip))
        for k, v in query_dict.items():
            logbook.debug("k:v, {} {}", k, v)

        def do_something(uuid):
            for i in range(1, 10):
                logbook.debug("do_something {} {}", uuid, i)
                gevent.sleep(3)
                gevent.idle()

        if not is_skip:
            tids = []
            for i in range(1, 3):
                uuid = self.next_uuid()
                tid = gevent.spawn(do_something, uuid)
                tids.append(tid)
            gevent.joinall(tids)
        else:
            logbook.debug("is_skip = true")
        return "hello world" + str(uid)

    def xxx(self):
        uid = self.next_uuid()
        return "xxx" + str(uid)

    def _on_bind_methods(self):
        self.web_ins.route("/hello", method="POST", callback=self.dd_cmd)
        self.web_ins.route("/hello", method="GET", callback=self.hello)
        # self.web_ins.route("/xxx", callback=self.xxx)
        self.web_ins.route("/ddcmd", method="POST", callback=self.dd_cmd)
        self.web_ins.route("/ddcmd", method="GET", callback=self.dd_cmd)
