import collections
import queue
import threading

import gevent
from gevent import monkey; monkey.patch_all()
import bottle
import os
from time import sleep

import logging

logging.basicConfig(level=logging.DEBUG)

wait_execute_fns = collections.deque()

def delay_execute(fn):
    wait_execute_fns.append(fn)

class WebApp(object):
    def __init__(self, web_ins):
        super(WebApp, self).__init__()
        self.web_ins = web_ins
        self._last_uuid = 0

    def next_uuid(self):
        self._last_uuid = self._last_uuid + 1
        return self._last_uuid

    def hello(self):
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

        def fn():
            body.put("reach")
            gevent.sleep(1)
            body.put("reach 2")
            import requests

            def fn2():
                # rsp = requests.get("http://www.baidu.com")
                rsp = requests.get("http://127.0.0.1:8080/hello")
                body.put("reach 3")
                body.put(str(rsp.status_code))
                body.put(rsp.text)
                body.put(StopIteration)
            delay_execute(fn2)
        delay_execute(fn)
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


class Task(object):
    def __init__(self, cb_fn, fn, *args, **kwargs):
        super(WebInstance, self).__init__()
        assert(self.fn)
        self.fn  = fn
        self.fn_args = args
        self.fn_kwargs = kwargs
        self.cb_fn = cb_fn
        self.fn_execute_succ = None
        self.fn_execute_rets = None

    def do_logic(self):
        pass

    def use_result(self):
        pass


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
        self.task_thread_is_exist = False

    def set_app(self, app):
        if self.app:
            self.app.reset_bind_urls()
        self.app = app
        if self.app:
            self.app.bind_urls()

    def add_task(self, cb_fn, fn, *args, **kwargs):
        self.task_lock.acquire()
        task = Task(cb_fn, fn, args, kwargs)
        self.task_list_in_main.append(task)
        self.task_lock.release()

    def start_task_thread(self):
        self.task_thread = threading.Thread(target=self._task_thread_loop)
        self.task_thread.start()

    def _task_thread_loop(self):
        while not self.task_thread_is_exist:
            need_sleep = False
            if self.task_lock.acquire(False):
                if len(self.task_list_in_main) > 0:
                    need_sleep = True
                else:
                    tmp = self.self.task_list_in_thread
                    self.task_list_in_thread = self.task_list_in_main
                    self.task_list_in_main = tmp
                self.task_lock.release()
            else:
                need_sleep = True
            if need_sleep:
                threading.Event.wait(0.001)
            else:
                for task in self.task_list_in_thread:
                    task.do_logic()
                if self.task_result_lock.acquire():
                    self.done_task_list.extend(self.task_list_in_thread)
                    self.task_list_in_thread.clear()
                    self.task_result_lock.release()

    def process_task_result(self):
        done_task_list = None
        if self.task_result_lock.acquire(False):
            done_task_list = self.done_task_list
            self.done_task_list = []
            self.task_result_lock.release()
        if done_task_list:
            for task in done_task_list:
                task.use_result()


# bottle.run(host='0.0.0.0', port=8080, server='gevent')

g_main_is_exist = False


def main_loop():
    global g_main_is_exist, wait_execute_fns
    while not g_main_is_exist:
        # print("app_loop")
        while len(wait_execute_fns) >  0:
            fn = wait_execute_fns.pop()
            fn()
        g_ins.process_task_result()
        gevent.sleep(2)


def test_trhead():
    g_ins.add_task()


if __name__ == '__main__':  # pragma: no coverage
    bt = bottle.Bottle()
    g_ins = WebInstance(bt)
    g_app = WebApp(g_ins)
    g_ins.set_app(g_app)

    g_ins.start_task_thread()
    main_thread = gevent.spawn(main_loop)
    bottle.run(app=g_ins.bt, host='0.0.0.0', port=8080, debug=True, reloader=True)
    g_main_is_exist = True
    gevent.joinall([main_thread])
