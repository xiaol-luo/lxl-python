import gevent

class GeventTask(gevent.Greenlet):
    def __init__(self):
        super(GeventTask, self).__init__(self._internal_logic)
        self.is_done = False
        self.error_num = 0
        self.error_msg = ""

    def _internal_logic(self):
        # 重写这里
        pass

    def set_done(self, error_num=0, error_msg=""):
        self.is_done = True
        self.error_num = error_num
        self.error_msg = error_msg

