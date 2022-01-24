import sys

from gevent import monkey; monkey.patch_all()
import collections
import queue
import threading

import gevent

import gevent.queue
import bottle
import os
from time import sleep
import typing

import logging

logging.basicConfig(level=logging.DEBUG)


class WebApp(object):
    def __init__(self, web_ins):
        super(WebApp, self).__init__()
        self.web_ins: WebInstance = web_ins
        self._last_uuid = 0

    def next_uuid(self):
        self._last_uuid = self._last_uuid + 1
        return self._last_uuid

    def hello(self):
        print("hello start!!")
        a = 1 + 1
        b = 2 + 1
        return "hello world" + str(self.next_uuid())

    def test_reset(self):
        # 这里无用
        self.reset_bind_urls()
        self.web_ins.bt.route("/reset", callback=self.test_reset)
        return "reset"

    def test_async(self):
        logging.info("test_async 1")
        body = gevent.queue.Queue()

        def fn(*args, **kwargs):
            print("test fn args, kwargs {0} {1}".format(args, kwargs))
            import requests
            rsp = requests.get("http://127.0.0.1:8080/hello")
            # rsp = requests.get("http://www.baidu.com")
            print("test fn args, kwargs pppppppppppppppp")
            return [str(rsp.status_code) + rsp.text]

        def cb_fn(is_ok, msg):
            print("cb_fn", is_ok, msg)
            body.put(msg)
            body.put(StopIteration)
            print("test cb_fn, " + msg)

        self.web_ins.add_task(cb_fn, fn, 1, 2, 3, a=1, b=2)
        logging.info("test_async 2")
        return body

    def test_download(self, file_name):
        return bottle.static_file(file_name, os.curdir, download=True)

    def reset_bind_urls(self):
        # 这个无效
        self.web_ins.bt.reset()

    def bind_urls(self):
        self.reset_bind_urls()
        self.web_ins.bt.route("/hello", callback=self.hello)
        self.web_ins.bt.route("/reset", callback=self.test_reset)
        self.web_ins.bt.route("/test_async", callback=self.test_async)
        self.web_ins.bt.route("/download/<file_name:path>", callback=self.test_download)


class WebInstance(object):
    def __init__(self, bt):
        super(WebInstance, self).__init__()
        self.bt = bt
        self.app = None
        from codes.libs.thread_task_mgr.thread_safe_task_mgr import ThreadSafeTaskMgr
        self.task_mgr = ThreadSafeTaskMgr()

    def set_app(self, app):
        if self.app:
            self.app.reset_bind_urls()
        self.app = app
        if self.app:
            self.app.bind_urls()

    def add_task(self, cb_fn, fn, *args, **kwargs):
        self.task_mgr.add_task(cb_fn, fn, *args, **kwargs)

    def process_task_logic(self):
        self.task_mgr.process_task_logic()

    def process_task_result(self):
        self.task_mgr.process_task_result()

if __name__ == '__main__':  # pragma: no coverage
    print("222")
    bt = bottle.Bottle()
    g_ins = WebInstance(bt)
    g_ins.set_app(WebApp(g_ins))

    # task_thread = threading.Thread(target=g_ins.process_task_logic, daemon=True)
    # task_thread.start()

    process_task_logic_thread = gevent.spawn(g_ins.process_task_logic)
    process_task_result_thread = gevent.spawn(g_ins.process_task_result)
    print("1111")
    bottle.run(app=g_ins.bt, server="gevent", host='0.0.0.0', port=8080, debug=True, reloader=True)
    gevent.joinall([process_task_logic_thread, process_task_result_thread])
