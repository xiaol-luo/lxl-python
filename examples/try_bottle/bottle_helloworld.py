import bottle
import sys
import os
import string

import logging 
logging.basicConfig(level=logging.DEBUG)

g_app = bottle.Bottle()

with g_app:
    @bottle.route('/greet')
    @bottle.route('/greet/<name>')
    def greet(name=''):
        if not name:
            name = bottle.request.get_cookie("username", 'stranger')
        return string.Template('Hello $name, how are you ?').substitute(name=name)

    @bottle.route('/params/<action>/<thing>')
    def do_something(action, thing):
        return string.Template("params $action $thing").substitute(action=action, thing=thing)

    @bottle.route('/filter/int/<num:int>')
    def filter_int(num):
        assert(isinstance(num, int))
        bottle
        return string.Template('you input int $num').substitute(num=num)

    @bottle.route('/filter/float/<num:float>')
    def filter_int(num):
        assert(isinstance(num, float))
        return string.Template('you input float $num').substitute(num=num)

    @bottle.route('/filter/path/<txt:path>')
    def filter_int(txt):
        return string.Template('you input path $txt').substitute(txt=txt)

    @bottle.route('/filter/re/<txt:re:[a-zA-Z0-9]+>')
    def filter_int(txt):
        return string.Template('you input re $txt').substitute(txt=txt)

    @bottle.get('/login')
    #@bottle.route('/login', method='GET')
    def login_get():
        xx = bottle.jinja2_template('login')
        return xx
        return '''
        <form action='/login' method='post'>
            UserName: <input name='username' type='text'/>
            Password: <input name='password' type='text'/>
            <input value='login' type='submit'/>
        </form>
        '''

    @bottle.post('/login')
    #bottle.route('/login', method='POST')
    def login_post():
        username = bottle.request.forms.get('username')
        password = bottle.request.forms.get('password')
        user_dict = {
            'xiaol-luo' : 'xiaolzz',
            'meimei' : 'meimei'
        }
        out_password = user_dict.get(username, None)
        if username and out_password == password:
            bottle.response.set_cookie("username", username)
            return bottle.redirect('/greet/{}'.format(username))
        return string.Template('username $name and password $password not match !').substitute(name=username, password=password) 

    @bottle.error(404)
    def error404(error):
        return 'nothing here, sorry !x'


    @bottle.route('/file/<filename:path>')
    def get_file(filename):
        return bottle.static_file(filename, os.curdir, download=True)

if __name__ == "__main__":
    ws_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ws_dir)
    #bottle.run(app=g_app, host='0.0.0.0', port=8080, debug=True)
    bottle.run(g_app, host='0.0.0.0', port=8080, debug=True)
