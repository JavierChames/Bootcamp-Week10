import json
from bottle import route, run,static_file,request

@route('/')
def index():
    return static_file("1.html", root='static/')



@route('/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='static/css')


@route('/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='static/js')

@route('/img/<filename:re:.*\.(jpg|jpeg)>')
def img(filename):
    return static_file(filename, root='static/img')


run(host='localhost', port=7000, debug=True,reloader=True)