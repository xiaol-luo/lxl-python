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

wait_execute_fns = collections.deque()


def delay_execute(fn):
    wait_execute_fns.append(fn)


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


FnParam = typing.ParamSpec("FnParam")
FnRet = typing.Optional[typing.List[typing.Any]]


class Task(object):
    fn: typing.Callable[[FnParam], FnRet]
    cb_fn: typing.Callable[[typing.Concatenate[bool, FnParam]], typing.NoReturn]
    fn_execute_succ: bool
    fn_execute_rets: FnRet
    fn_args: FnParam.args
    fn_kwargs: FnParam.kwargs

    def __init__(self, cb_fn, fn, *args, **kwargs):
        super(Task, self).__init__()
        self.fn = fn
        assert (callable(self.fn))
        self.fn_args = args
        self.fn_kwargs = kwargs
        self.cb_fn = cb_fn
        self.fn_execute_succ = None
        self.fn_execute_rets = None

    def do_logic(self):
        try:
            ret = self.fn(*self.fn_args, **self.fn_kwargs)
            if ret is not None:
                self.fn_execute_rets = ret
            self.fn_execute_succ = True
        except Exception as e:
            self.fn_execute_succ = False
            self.fn_execute_rets = [str(e)]

    def use_result(self):
        if callable(self.cb_fn):
            if self.fn_execute_rets is not None:
                self.cb_fn(self.fn_execute_succ, *self.fn_execute_rets)
            else:
                self.cb_fn(self.fn_execute_succ)


class WebInstance(object):
    def __init__(self, bt):
        super(WebInstance, self).__init__()
        self.bt = bt
        self.app = None
        self.task_lock = threading.Lock()
        self.task_result_lock = threading.Lock()
        self.task_list_in_thread = []
        self.task_list_in_main = []
        self.done_task_list = []
        self.task_thread = None
        self.process_task_is_exist = False

    def set_app(self, app):
        if self.app:
            self.app.reset_bind_urls()
        self.app = app
        if self.app:
            self.app.bind_urls()

    def add_task(self, cb_fn, fn, *args, **kwargs):
        print("add_task")
        self.task_lock.acquire()
        task = Task(cb_fn, fn, args, kwargs)
        self.task_list_in_main.append(task)
        self.task_lock.release()

    def process_task_logic(self):
        sleep_ev = threading.Event()
        while not self.process_task_is_exist:
            need_sleep = False
            if self.task_lock.acquire(False):
                if len(self.task_list_in_main) <= 0:
                    need_sleep = True
                else:
                    tmp = self.task_list_in_thread
                    self.task_list_in_thread = self.task_list_in_main
                    self.task_list_in_main = tmp
                self.task_lock.release()
            else:
                need_sleep = True
            if not need_sleep:
                print("need_sleep:{0}".format(self.task_list_in_thread))
            if need_sleep:
                sleep_ev.wait(0.01)
            else:
                for task in self.task_list_in_thread:
                    print("task.do_logic() start")
                    task.do_logic()
                    print("task.do_logic() end")
                if self.task_result_lock.acquire():
                    self.done_task_list.extend(self.task_list_in_thread)
                    self.task_list_in_thread.clear()
                    self.task_result_lock.release()

    def process_task_result(self):
        sleep_ev = threading.Event()
        while not self.process_task_is_exist:
            need_sleep = True
            done_task_list = None
            if self.task_result_lock.acquire(False):
                if len(self.done_task_list) > 0:
                    need_sleep = False
                    done_task_list = self.done_task_list
                    self.done_task_list = []
                self.task_result_lock.release()
            if not need_sleep:
                if done_task_list:
                    for task in done_task_list:
                        task.use_result()
            else:
                sleep_ev.wait(0.01)


# bottle.run(host='0.0.0.0', port=8080, server='gevent')

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
