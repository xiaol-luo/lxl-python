from __future__ import annotations
import typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # 解决type hint导致的循环引用问题
    from .gevent_cmd import GeventCmd
    Fn_GeventCmd_Handle_Content = typing.Callable[[GeventCmd, str], typing.NoReturn]
    Fn_GeventCmd_Handle_Done = typing.Callable[[GeventCmd], typing.NoReturn]

import gevent
import gevent.subprocess
import shlex
import io
import typing


class GeventCmd(object):
    process: gevent.subprocess.Popen
    cmd: str
    env: dict
    _handle_done: Fn_GeventCmd_Handle_Done
    _handle_stdout_content: Fn_GeventCmd_Handle_Content
    _handle_stderr_content: Fn_GeventCmd_Handle_Content
    _out_content: io.StringIO
    _error_content: io.StringIO
    _gl_process: gevent.greenlet.Greenlet
    _gl_read_stdout: gevent.greenlet.Greenlet
    _gl_read_stdout: gevent.greenlet.Greenlet

    def __init__(self, cmd, handle_done: Fn_GeventCmd_Handle_Done = None,
                 handle_stdout_content: Fn_GeventCmd_Handle_Content = None,
                 handle_stderr_content: Fn_GeventCmd_Handle_Content = None,
                 env=None, capture_output=False):
        super(GeventCmd, self).__init__()
        self.process = None
        self.cmd = cmd
        self.env = env
        self._handle_done = handle_done
        self._handle_stdout_content = handle_stdout_content
        self._handle_stderr_content = handle_stderr_content
        self.capture_output = capture_output
        self._out_content = None
        self._error_content = None
        self._gl_process = None
        self._gl_read_stdout = None
        self._gl_read_stderr = None

    def execute(self, input=None, timeout=None, is_async=False):
        if self.process:
            raise Exception("GeventCmd {} already executed".format(self.cmd))
        self.process = gevent.subprocess.Popen(
            shlex.split(self.cmd),
            env=self.env,
            shell=True,
            universal_newlines=True,
            text=True,
            stdout=gevent.subprocess.PIPE,
            stderr=gevent.subprocess.PIPE)
        if not is_async:
            return self._manage_execute(input, timeout)
        else:
            self._gl_process = gevent.spawn(self._manage_execute, input, timeout)
            return None

    def _manage_execute(self, input=None, timeout=None):
        if not self.process:
            raise Exception("GeventCmd {} not executed".format(self.cmd))
        if self._gl_read_stderr or self._gl_read_stderr:
            return
        if self.process.returncode is not None:
            return
        if self.capture_output:
            self._error_content = io.StringIO()
            self._out_content = io.StringIO()
        self._gl_read_stdout = gevent.spawn(self._read_stdout)
        self._gl_read_stderr = gevent.spawn(self._read_stderr)
        self.process.communicate(input, timeout)
        # self.process.wait()
        if self._gl_read_stderr and not self._gl_read_stdout.dead:
            self._gl_read_stderr.kill()
        if self._gl_read_stdout and not self._gl_read_stdout.dead:
            self._gl_read_stdout.kill()
        self._gl_read_stderr = None
        self._gl_read_stderr = None
        self._gl_process = None
        self.process.stdout.close()
        self.process.stderr.close()
        if self._handle_done:
            self._handle_done(self)
        return self.process.returncode

    def wait(self, timeout=None):
        return self.process.wait(timeout)

    def kill(self):
        if not self.process:
            return
        if self.process.returncode is not None:
            return
        self.process.kill()
        to_join = []
        if self._gl_read_stdout:
            to_join.append(self._gl_read_stdout)
        if self._gl_read_stderr:
            to_join.append(self._gl_read_stderr)
        if self._gl_process:
            to_join.append(self._gl_process)
        gevent.joinall(to_join)
        self._gl_read_stderr = None
        self._gl_read_stderr = None
        self._gl_process = None

    @property
    def return_code(self):
        if self.process is None:
            return
        return self.process.returncode

    @property
    def out_text(self):
        if self._out_content is None:
            return
        return self._out_content.getvalue()

    @property
    def error_text(self):
        if self._error_content is None:
            return
        return self._error_content.getvalue()

    def _read_stdout(self):
        for txt in self.process.stdout:
            if self._out_content is not None:
                self._out_content.write(txt)
            if self._handle_stdout_content:
                self._handle_stdout_content(self, txt)

    def _read_stderr(self):
        for txt in self.process.stderr:
            if self._error_content is not None:
                self._error_content.write(txt)
            if self._handle_stderr_content:
                self._handle_stderr_content(self, txt)
