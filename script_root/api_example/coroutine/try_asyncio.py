# 参考这个 https://zhuanlan.zhihu.com/p/59671241

import asyncio
import subprocess


async def create_proc(loop):
    proc: asyncio.subprocess.Process = await asyncio.create_subprocess_shell("ping -n 30 127.0.0.1", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc


async def run_proc(proc: asyncio.subprocess.Process):
    await proc.wait()
    print("run cmd end", proc.returncode)


async def read_proc_stdout(proc: asyncio.subprocess.Process):
    while not proc.stdout.at_eof():
        txt = await proc.stdout.readline()
        print("stdout", txt)


async def read_proc_stderr(proc: asyncio.subprocess.Process):
    while not proc.stderr.at_eof():
        txt = await proc.stderr.readline()
        print("stderr", txt)


loop = asyncio.get_event_loop()
proc = loop.run_until_complete(create_proc(loop))
loop.create_task(run_proc(proc))
loop.create_task(read_proc_stdout(proc))
loop.create_task(read_proc_stderr(proc))

while True:
    loop.run_until_complete(asyncio.sleep(0.00001))
