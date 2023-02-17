import sys
import os
import typing
import pathlib
import importlib
import argparse
import logbook


def log_formatter(record: logbook.LogRecord, handler: logbook.Handler)->typing.NoReturn:
    record.lineno
    record.func_name
    pass

log_format_string = '[{record.time:%Y-%m-%d %H:%M:%S.%f%z}] {record.level_name}: [{record.filename}:{record.lineno}] {record.message}'
logbook.StreamHandler(sys.stdout, format_string=log_format_string).push_application()


def split_args(arg_list: typing.List[str]) -> typing.Tuple[typing.List[str], typing.List[str]]:
    entrance_args = None
    exec_args = None
    try:
        split_idx = arg_list.index("__split_flag__")
        entrance_args = arg_list[:split_idx]
        exec_args = arg_list[split_idx+1:]
    except Exception as e:
        logbook.exception(e)
        entrance_args = arg_list
        exec_args = []
    return entrance_args, exec_args


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--work_dir", help="working directory")
arg_parser.add_argument("--search_dir", nargs="*", help="python script search path")
arg_parser.add_argument("--exec", required=True, nargs="+", help="exec format path.to.module.func_name or path.to.module.")

entrance_args, exec_args = split_args(sys.argv[1:])
# logbook.debug("entrance_args, exec_args {} {}", entrance_args, exec_args)
parse_ret = arg_parser.parse_args(entrance_args)
'''
for (k, v) in vars(parse_ret).items():
    logbook.debug("k, v: {} {}", k, v)
'''

if parse_ret.work_dir:
    work_dir_path = pathlib.Path(parse_ret.work_dir)
    if not work_dir_path.is_dir():
        logbook.error("work dir is not exist: {}", work_dir_path.absolute().as_posix())
        sys.exit(-10000)
    else:
        logbook.debug("work dir is {}", work_dir_path.absolute().as_posix())
        os.chdir(work_dir_path.as_posix())

if parse_ret.search_dir:
    for elem in parse_ret.search_dir:
        sys.path.append(os.path.abspath(elem))
logbook.debug("sys.path is {}", sys.path)

if not parse_ret.exec:
    logbook.error("parse_ret.exec is empty")
    sys.exit(-20100)

for elem in parse_ret.exec:
    idx = str.rfind(elem, ".")
    if -1 == idx:
        logbook.error("parse_ret.exec format is invalid: {}", elem)
        sys.exit(-20200)
    module_name = elem[:idx]
    if idx == len(elem) - 1:
        fun_name = None
    else:
        fun_name = elem[idx+1:]

    exec_module = importlib.import_module(module_name)
    if not exec_module:
        logbook.error("not found exec_module {}", module_name)
        sys.exit(-20300)
    if fun_name:
        exec_fun = exec_module.__dict__.get(fun_name)
        if not exec_fun:
            logbook.error("not found exec_fun {}", elem)
            sys.exit(-20400)
        exec_fun(exec_args)

