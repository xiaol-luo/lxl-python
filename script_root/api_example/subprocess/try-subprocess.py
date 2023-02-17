import logging
import os
import subprocess
import shlex

logging.basicConfig(level=logging.DEBUG)

ret = os.system("dir")
logging.debug(ret)

ret = os.popen("dir")
logging.debug("--------------------------")
for i in ret:
    logging.debug(i)
logging.debug(ret)

logging.debug("++++++++++++++++++++++++++++++")
status, ret = subprocess.getstatusoutput("dir")
logging.debug("status %s, ret %s", status, ret)

ret = subprocess.run("dir", shell=True,
                     universal_newlines=True, stderr=subprocess.PIPE, 
                     stdout=subprocess.PIPE, timeout=2)
logging.debug(ret)

ret = subprocess.run(shlex.split('dir'), shell=True,
                     universal_newlines=True, stderr=subprocess.PIPE, 
                     stdout=subprocess.PIPE, timeout=2)
logging.debug(ret)

ret = subprocess.Popen(['dir'], shell=True, 
                    universal_newlines=True, stdout=subprocess.PIPE)
ret.communicate()
logging.debug("%s %s", ret.returncode, ret.stdout)

# subprocess.call -> returncode
#subprocess.check_call -> returncode
#subprocess.check_output -> stdout
#subprocess.getoutput ->stdout
#subprocess.getstatusoutput ->returncode, stdout



