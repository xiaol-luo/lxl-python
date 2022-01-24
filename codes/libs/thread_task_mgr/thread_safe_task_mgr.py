import threading
import typing

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


class ThreadSafeTaskMgr(object):
    def __init__(self):
        super(ThreadSafeTaskMgr, self).__init__()
        self.task_lock = threading.Lock()
        self.task_result_lock = threading.Lock()
        self.task_list_in_thread = []
        self.task_list_in_main = []
        self.done_task_list = []
        self.process_task_is_exit = False

    def add_task(self, cb_fn, fn, *args, **kwargs):
        # print("add_task {0}, {1}".format(args, kwargs))
        self.task_lock.acquire()
        task = Task(cb_fn, fn, *args, **kwargs)
        self.task_list_in_main.append(task)
        self.task_lock.release()

    def process_task_logic(self):
        sleep_ev = threading.Event()
        while not self.process_task_is_exit:
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
            if need_sleep:
                sleep_ev.wait(0.01)
            else:
                for task in self.task_list_in_thread:
                    task.do_logic()
                if self.task_result_lock.acquire():
                    self.done_task_list.extend(self.task_list_in_thread)
                    self.task_list_in_thread.clear()
                    self.task_result_lock.release()

    def process_task_result(self):
        sleep_ev = threading.Event()
        while not self.process_task_is_exit:
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
    task_mgr = ThreadSafeTaskMgr()
    process_task_logic_thread = threading.Thread(target=task_mgr.process_task_logic, daemon=True)
    process_task_logic_thread.start()

    process_task_result_thread = threading.Thread(target=task_mgr.process_task_result, daemon=True)
    process_task_result_thread.start()

    def task_logic(task_id, task_id_plus_one, kw_task_id="default_kw_task_id"):
        # print("task_logic", str(task_id), str(task_id_plus_one), str(kw_task_id))
        return [task_id, task_id_plus_one, kw_task_id]

    def task_cb(task_ok, ret_task_id, ret_task_id_plus_one, kw_task_id):
        # print("task_cb", str(task_ok), str(ret_task_id), str(ret_task_id_plus_one), str(kw_task_id))
        pass

    last_id = 0

    def next_id():
        global last_id
        last_id = last_id + 1
        return  last_id


    test_loop_is_exit = False

    def test_loop():
        sleep_ev = threading.Event()
        while not test_loop_is_exit:
            sleep_ev.wait(0.1)
            task_id = next_id()
            task_id_plus_one = task_id + 1
            kw_task_id = "kw_task_id_" + str(task_id)
            # print("test one way")
            # task_mgr.add_task(task_cb, task_logic, task_id, task_id_plus_one, kw_task_id)
            # print("test another way")
            task_mgr.add_task(task_cb, task_logic, task_id, task_id_plus_one, kw_task_id=kw_task_id)


    test_loop_thread = threading.Thread(target=test_loop, daemon=True)
    test_loop_thread.start()

    def signal_handler(sig_num, frame):
        print("signal_handler " + str(sig_num))
        global test_loop_is_exit
        test_loop_is_exit = True

    import signal
    signal.signal(signal.SIGINT, signal_handler)  # windows下无效
    signal.signal(signal.SIGTERM, signal_handler)  # windows下无效

    test_loop_thread.join()
    task_mgr.process_task_is_exit = True
    process_task_logic_thread.join()
    process_task_result_thread.join()
