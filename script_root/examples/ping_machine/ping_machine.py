import subprocess
import sys
import typing
import imgui
import pyglet
from imgui.integrations.pyglet import create_renderer
import argparse
import datetime
import logbook
import queue
import shlex
import threading
log_format_string = '[{record.time:%Y-%m-%d %H:%M:%S.%f%z}] {record.level_name}: [{record.filename}:{record.lineno}] {record.message}'
logbook.StreamHandler(sys.stdout, format_string=log_format_string).push_application()


class AppBase(object):
    app_window: pyglet.window.Window
    gui_context: imgui.integrations.pyglet.PygletProgrammablePipelineRenderer

    def __init__(self):
        self.app_window = None
        self.gui_impl = None
        self.is_setup = False
        self.gui_context = None
        self.menu_bar_height = 25
        pass

    def setup(self, *args, **kwargs):
        self.app_window = pyglet.window.Window(width=1080, height=960, resizable=True)
        self.gui_context = imgui.create_context()
        self.gui_impl = create_renderer(self.app_window)
        pyglet.clock.schedule_interval(self._main_loop, 1 / 60)
        self.is_setup = True
        self._on_setup(*args, **kwargs)

    def run(self):
        pyglet.app.run()
        self.reset()

    def shutdown(self):
        pyglet.app.exit()

    def reset(self):
        self._on_reset()
        # 下边这些变量貌似只是判断是否为空都直接退出程序
        self.gui_impl = None
        self.app_window = None
        self.gui_context = None
        self.is_setup = False

    def _main_loop(self, dt):
        imgui.new_frame()
        self._on_main_loop(dt)
        self.app_window.clear()
        imgui.render()
        self.gui_impl.render(imgui.get_draw_data())

    def _on_reset(self):
        pass

    def _on_setup(self, *args, **kwargs):
        pass

    def _on_main_loop(self, dt):
        pass

    @property
    def app_width(self) -> float:
        return self.app_window.width - 10

    @property
    def app_height(self) -> float:
        return self.app_window.height

    def cal_width(self, ratio) -> float:
        ret = self.app_width * ratio
        ret = max(0, ret)
        return ret

    def cal_height(self, ratio, sub_menu_bar: bool = False) -> float:
        if sub_menu_bar:
            ret = (self.app_height - self.menu_bar_height) * ratio
        else:
            ret = self.app_height * ratio
        ret = max(0, ret)
        return ret


class MachineState(object):
    def __init__(self):
        self.ip = None
        self.is_alive = False
        self.last_check_time = ""


class PingWorker(object):
    queue: queue.SimpleQueue
    thread: threading.Thread
    thread_event: threading.Event
    process: subprocess.Popen
    ip: str
    content_lines: typing.List[str]

    def __init__(self):
        self.thread = None
        self.ip = None
        self.thread_event = None
        self.queue = None
        self.process = None
        self.content_lines = []
        self.error_lines = []


    def run(self, ip):
        self.ip = ip
        self.process = subprocess.Popen(
            shlex.split("ping -n 3 {0}".format(ip)),
            shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        self.queue = queue.SimpleQueue()
        self.thread_event = threading.Event()
        self.thread = threading.Thread(target=PingWorker._do_ping, args=(self.process.stdout, self))
        self.thread.start()

    @staticmethod
    def _do_ping(a, worker):
        if worker.process.stdout:
            for line in iter(worker.process.stdout.readline, b''):
                worker.queue.put(line)
                if worker.thread_event.is_set():
                    break

    def is_runing(self):
        if self.process and  self.process.returncode is None:
            return True
        return  False

    def poll(self):
        if self.is_runing():
            self.process.poll()
        else:
            self.thread_event.set()
            for line in self.process.stderr.readlines():
                self.error_lines.append(line.decode("GKB"))
        if self.queue is not None and self.content_lines is not None:
            try:
                line = self.queue.get_nowait()
                self.content_lines.append(line.decode('GBK'))
            except queue.Empty:
                pass


class AppPingMachine(AppBase):
    machin_state_list: typing.List[MachineState]
    _check_task_list: typing.List[str]
    _ping_worker: PingWorker

    def __init__(self):
        super(AppPingMachine, self).__init__()
        self.machine_state_list = []
        self._last_check_all_time = datetime.datetime.min
        self._check_all_span = datetime.timedelta(hours=1, seconds=5)
        self._check_task_list = []
        self._ping_worker = None
        self._error_msg = ""

    def _on_setup(self, *args, **kwargs):
        self.machine_state_list.clear()
        host_list = kwargs["host_list"]
        for ip in host_list:
            state = MachineState()
            self.machine_state_list.append(state)
            state.ip = ip
            state.last_check_time = ""
        self._last_check_all_time = datetime.datetime.min

    def _on_main_loop(self, dt):
        imgui.begin("check alive", True,
                    imgui.WINDOW_MENU_BAR | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_MOVE)
        imgui.set_window_size(self.cal_width(0.8), self.cal_height(0.8))
        if imgui.button("check all"):
            self._last_check_all_time = datetime.datetime.min
        imgui.begin_child("machine list", 0, 0, True)
        for item in self.machine_state_list:
            imgui.begin_group()
            if imgui.button("check " + item.ip):
                self._check_task_list.append(item.ip)
            imgui.same_line()
            imgui.text("state is {0}, check time {1}".format(item.is_alive and "alive" or "dead", item.last_check_time))
            imgui.end_group()
        imgui.end_child()
        is_opened = False
        if self._ping_worker:
            is_opened, is_visual = imgui.begin_popup_modal("ping_machine", True)
            if is_opened:
                imgui.text("wait ping {0}".format(self._ping_worker.ip))
                for line in self._ping_worker.content_lines:
                    imgui.text(line)
                imgui.end_popup()
            else:
                imgui.open_popup("ping_machine")
        if not self._ping_worker and self._error_msg:
            is_opened, is_visual = imgui.begin_popup_modal("error_msg", True)
            if is_opened:
                imgui.text(self._error_msg)
                imgui.end_popup()
            else:
                self._error_msg = ""
        self._check_handle_task()
        self._try_check_all()
        imgui.end()

    def _try_check_all(self):
        if len(self._check_task_list) > 0:
            return
        if datetime.datetime.now() - self._last_check_all_time > self._check_all_span:
            self._last_check_all_time = datetime.datetime.now()
            for item in self.machine_state_list:
                self._check_task_list.append(item.ip)

    def _check_handle_task(self):
        if self._ping_worker is None:
            if len(self._check_task_list) > 0:
                ip = self._check_task_list.pop(0)
                self._ping_worker = PingWorker()
                self._ping_worker.run(ip)
        else:
            self._ping_worker.poll()
            if not self._ping_worker.is_runing():
                ping_worker = self._ping_worker
                self._ping_worker = None
                is_alive = True
                if len(ping_worker.error_lines) > 0:
                    is_alive = False
                for line in ping_worker.content_lines:
                    if line.find("请求超时") >= 0:
                        is_alive = False
                    if line.find("找不到主机") >= 0:
                        is_alive = False
                if not is_alive:
                    self._error_msg += "".join(ping_worker.error_lines) + "".join(ping_worker.content_lines)
                    imgui.open_popup("error_msg")
                logbook.debug("out is {} ", ping_worker.content_lines)
                logbook.debug("error is {} ", ping_worker.error_lines)
                logbook.debug("is alive {}", is_alive)
                for item in self.machine_state_list:
                    if item.ip == ping_worker.ip:
                        item.is_alive = is_alive
                        item.last_check_time = datetime.datetime.now()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--host", nargs="+", help="machine ip")
    parse_ret = arg_parser.parse_args(sys.argv[1:])
    for (k, v) in vars(parse_ret).items():
        logbook.debug("parse_ret k, v: {} {}", k, v)
    app = AppPingMachine()
    # for v in parse_ret.host:
        # app.ip_list.append(v)
    app.setup(host_list=parse_ret.host)
    app.run()

