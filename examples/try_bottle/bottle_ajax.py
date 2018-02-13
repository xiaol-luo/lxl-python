import bottle
import sys
import os
import string
import collections
import threading
import subprocess
import shlex

import logging 
logging.basicConfig(level=logging.DEBUG)

g_app = bottle.Bottle()

with g_app:
    @bottle.route("/")
    @bottle.view('ajax_index.html')
    def index_page():
        params = {
            "param": 12456679,
            "times": 10
        }
        return params
        #ret = bottle.template('ajax_index.html', params)
        #return ret 
        
    
    @bottle.route('/load_xml_doc')
    def load_xml_doc():
        return "ajax return string"

    class ExcuteCmdState(object):
        def __init__(self):
            self.running = False
            self.file_name = None

    g_excute_cmd_ret = ExcuteCmdState()
    
    @bottle.route('/excute_cmd')
    def excute_cmd():
        global g_excute_cmd_ret
        if not g_excute_cmd_ret.running:
            g_excute_cmd_ret.running = True
            g_excute_cmd_ret.file_name = "ret.txt"
            g_excute_cmd_ret.file_content = ""
            def execute_fn():
                subprocess.call("python test_cmd.py 2>&1 1>{}".format(g_excute_cmd_ret.file_name), shell=True)
                g_excute_cmd_ret.running = False
            threading.Timer(0, execute_fn).start()
        return "command executing"
    
    @bottle.route('/query_cmd_ret')
    def query_cmd_ret():
        global g_excute_cmd_ret
        next_idx = int(bottle.request.query.get("next_idx"))
        ret = ""
        content = ""
        if g_excute_cmd_ret and g_excute_cmd_ret.file_name:
            with open(g_excute_cmd_ret.file_name, 'r') as f:
                content = f.read()
        if next_idx < len(content):
            ret = content[next_idx:]
        return {'index': next_idx, "ret" : ret, "running": g_excute_cmd_ret.running}


if __name__ == "__main__":
    ws_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ws_dir)
    bottle.run(app=g_app, host='0.0.0.0', port=8080, debug=True)
    #bottle.run(g_app, host='0.0.0.0', port=8080, debug=True, reloader=True)