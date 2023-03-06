import json
import time

import requests
import logbook
import typing

class DDRobotClient(object):
    def __init__(self, robot_key, robot_secret, send_url):
        super(DDRobotClient, self).__init__()
        self._robot_key = robot_key
        self._robot_secret = robot_secret
        self._send_url = send_url
        self._token = None
        self._token_timeout_sec = 0

    def fetch_token(self, is_force=False):
        if not is_force and time.time() <= self._token_timeout_sec and self._token:
            return True

        query_url = "https://oapi.dingtalk.com/gettoken?appkey={robot_key}&appsecret={robot_secret}".format(
            robot_key = self._robot_key,
            robot_secret = self._robot_secret
        )
        logbook.debug("1111111111111 {}", query_url)
        rsp: requests.Response = requests.get(query_url)
        logbook.debug("222222222222222222")
        if not rsp.ok:
            logbook.error("fetch token fail, rsp.status_code {}", rsp.status_code)
            return False
        dt: typing.Dict = rsp.json()
        error_code = dt.get("errcode", -1)
        error_msg = dt.get("errmsg", -1)
        access_token = dt.get("access_token", None)
        expires_in = int(dt.get("expires_in", 0))
        if 0 != error_code:
            logbook.error("fetch_token fail, {} {}", error_code, error_msg)
            return False
        self._token = access_token
        self._token_timeout_sec = time.time() + expires_in
        logbook.debug("dt is {} {}", type(dt), dt)
        return True

    def send_text(self, msg):
        # self.fetch_token()
        # query_url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(self._token)
        query_url = self._send_url
        header_dt = {
            "Content-Type": "application/json",
        }
        body_dt = {
            "msgtype": "text",
            "text": {
                "content": "robot:\n" + msg
            },
        }
        rsp: requests.Response = requests.request("POST", query_url, headers=header_dt, json=body_dt)
        logbook.debug("send text rsp {}  {}", query_url, rsp.text)
