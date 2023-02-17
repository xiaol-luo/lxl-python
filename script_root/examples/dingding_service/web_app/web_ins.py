from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # 解决type hint导致的循环引用问题
    from .web_app import WebApp

from ..bottle import Bottle
from ..bottle import request as bt_request

from libs.thread_task_mgr.thread_safe_task_mgr import ThreadSafeTaskMgr
import gevent
import examples.dingding_service.bottle as bottle


class WebIns(object):
    _bt: Bottle
    app: WebApp
    request: bt_request
    task_mgr: ThreadSafeTaskMgr

    def __init__(self, bt):
        super(WebIns, self).__init__()
        self._bt = bt
        self.app = None
        self.request = bt_request
        self.task_mgr = ThreadSafeTaskMgr()

    def set_app(self, app: WebApp):
        assert self.app is None
        self.app = app
        self.app.bind_methods()

    def route(self, path=None, method='GET', callback=None, name=None, apply=None, skip=None, **config):
        self._bt.route(path=path, method=method, callback=callback, name=name, apply=apply, skip=skip, **config)

    def reset_routes(self, route=None):
        self._bt.reset(route=route)

    def add_task(self, cb_fn, fn, *args, **kwargs):
        self.task_mgr.add_task(cb_fn, fn, *args, **kwargs)

    def _process_task_logic(self):
        self.task_mgr.process_task_logic()

    def _process_task_result(self):
        self.task_mgr.process_task_result()

    def run(self,
            host='127.0.0.1',
            port=8080,
            interval=1,
            reloader=False,
            quiet=False,
            plugins=None,
            debug=None,
            config=None, **kargs):
        process_task_logic_thread = gevent.spawn(self._process_task_logic)
        process_task_result_thread = gevent.spawn(self._process_task_result)
        bottle.run(self._bt, "gevent", host, port, interval, reloader, quiet, plugins, debug, config, **kargs)
        gevent.joinall([process_task_logic_thread, process_task_result_thread])
