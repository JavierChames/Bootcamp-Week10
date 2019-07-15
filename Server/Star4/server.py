import json
from bottle import route, run,static_file,request

@route('/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='static/js')


@route('/')
def index():
    return static_file("1.html", root='static/')


@route('/img/<filename:re:.*\.(jpg|jpeg)>')
def img(filename):
    return static_file(filename, root='static/img')


run(host='localhost', port=7001, debug=True,reloader=True)