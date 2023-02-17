# from gevent import monkey
# monkey.patch_all()

import logbook
import sys
import typing
from libs.gevent_ext.gevent_cmd import GeventCmd

def log_formatter(record: logbook.LogRecord, handler: logbook.Handler)->typing.NoReturn:
    record.lineno
    record.func_name
    pass

log_format_string = '[{record.time:%Y-%m-%d %H:%M:%S.%f%z}] {record.level_name}: [{record.filename}:{record.lineno}] {record.message}'
logbook.StreamHandler(sys.stdout, format_string=log_format_string).push_application()


def print_line(p, line):
    logbook.debug("uuid: line {}", line)

def print_line_2(p, line):
    logbook.debug("xxxxx line {}", line)

logbook.debug("reach here 1")


cmd_2 = GeventCmd("ping -n 10 www.baidu.com", handle_stdout_content=print_line_2,
                handle_stderr_content=print_line_2, capture_output=True)
cmd_2.execute(is_async=True)


cmd = GeventCmd("ping -n 20  www.baidu.com", handle_stdout_content=print_line,
                handle_stderr_content=print_line, capture_output=True)
cmd.execute()

logbook.debug("cmd out_text {}", cmd.out_text)
logbook.debug("cmd error_text {}", cmd.error_text)
logbook.debug("reach here 2")
