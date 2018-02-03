import sys
import shlex
import subprocess
import logging
import os

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging

pyfile_dir = os.path.join(os.path.abspath(os.path.curdir), "examples/try-ply/lpy-protobuf").replace('\\', '/')

#parse proto
parse_file_path = os.path.join(pyfile_dir, "lpy_protobuf.py").replace('\\', '/')
lpy_parse_cmd = 'python {0}'.format(parse_file_path)
prase_proto_p = subprocess.Popen(shlex.split(lpy_parse_cmd), bufsize=1024, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
(out_str, err_str) = prase_proto_p.communicate()
return_code = prase_proto_p.returncode
if return_code:
    log.error("parse proto file fail errno : {0}".format(return_code))
    sys.exit(-1)
log.debug("parse proto file success")

#gen code
gencode_file_path = os.path.join(pyfile_dir, "lpy_gencode.py").replace('\\', '/')
lpy_gencode_cmd = 'python {0}'.format(gencode_file_path)
gencode_p = subprocess.Popen(shlex.split(lpy_gencode_cmd), bufsize=1024, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
(out_str, err_str) = gencode_p.communicate()
return_code = gencode_p.returncode
if return_code:
    log.error("gen code errno : {0}".format(return_code))
    sys.exit(-1)
log.debug("gen code success")
log.debug(out_str)






