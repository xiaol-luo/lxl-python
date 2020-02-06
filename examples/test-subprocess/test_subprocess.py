import sys
import os
import logging
import socket
import subprocess
import shlex

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging

test_python_p = subprocess.Popen(shlex.split(" .py 1"), bufsize=1024, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
(out_str, err_str) = test_python_p.communicate()
return_code = test_python_p.returncode

test_batch_p = subprocess.Popen(shlex.split("test_ret.bat 1"), bufsize=1024, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
(out_str, err_str) = test_batch_p.communicate()
return_code = test_batch_p.returncode 

