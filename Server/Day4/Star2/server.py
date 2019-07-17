from bottle import static_file, run, jinja2_view, get,request,route
from jinja2 import Template
from functools import partial
fname=""
lname=""

view = partial(jinja2_view, template_lookup=['templates'])

# Static routes:
@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./static/js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./static/css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./static/images")
    
@route('/')
def index():
    return static_file("singup.html", root='templates/') 

@route("/add" , method="POST")
@view("welcome.html")
def welcome():
     fname=request.forms.get("usrname")
     lname= request.forms.get("lstname")
     return {"firstname": fname,"lastname": lname}

if __name__ == "__main__":
    run(host="localhost", port=7000, debug=True, reloader=True)
