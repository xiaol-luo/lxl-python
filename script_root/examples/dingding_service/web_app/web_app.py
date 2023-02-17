from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: # 解决type hint导致的循环引用问题
    from .web_ins import WebIns


class WebApp(object):
    web_ins: WebIns

    def __init__(self, web_ins: WebIns):
        super(WebApp, self).__init__()
        self.web_ins = web_ins

    def unbind_methods(self):
        # 这个无效
        self._on_unbind_methods()
        self.web_ins.reset_routes()

    def bind_methods(self):
        self.unbind_methods()
        self._on_bind_methods()
        # self.web_ins.bt.route("/hello", callback=self.hello)

    def _on_bind_methods(self):
        pass

    def _on_unbind_methods(self):
        pass


