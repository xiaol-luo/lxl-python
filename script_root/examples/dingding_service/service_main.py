
def main(arg_list):
    from gevent import monkey
    monkey.patch_all()

    from .web_app import WebIns
    from .app_dd import AppDD
    from .bottle import Bottle
    bt = Bottle()
    g_ins = WebIns(bt)
    g_ins.set_app(AppDD(g_ins))
    g_ins.run(host='0.0.0.0', port=8080, debug=True, reloader=True)

