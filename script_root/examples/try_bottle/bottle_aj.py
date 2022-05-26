import bottle
import os
import sys
import string
import collections
import threading
import subprocess
import shlex
import logging #运行日志包

logging.basicConfig(level=logging.DEBUG)

g_app = bottle.Bottle()

with g_app:
    @bottle.route("/")
    def index_page():
        params = {
            "params": 123456679,
            "times" : 10
        }
        #return params
        ret = bottle.template('aj_index.html', params)
        return ret

if __name__ == "__main__":
    ws_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ws_dir)
    #bottle.run(app=g_app, host='0,0,0,0', port=8080, debug=True)
    bottle.run(g_app, host='0.0.0.0', port=8080, debug=True, reloader=True)




