import json
from bottle import route, run, static_file, request, response,error

@error(404)
def error404(error):
    return static_file("error.html", root='static/')




@route('/found')
def index():
    if response.status_code == 200:
        return static_file("found.html", root='static/')
    

     


@route('/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='static/css')


@route('/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='static/js')


@route('/static/img/<filename:re:.*\.(jpg|jpeg)>')
def img(filename):
    # print(filename)
    return static_file(filename, root='/static/img')


run(host='localhost', port=7000, debug=True, reloader=True)
