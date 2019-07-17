from bottle import static_file, run, jinja2_view, get
from jinja2 import Template
from functools import partial

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

count=0
# Dynamic routes:
@get("/")
def index():
    global count
    count= count+1
    template=Template('The server has been accedded {{mycount}}!')
    return template.render(mycount=count)

if __name__ == "__main__":
    run(host="localhost", port=7000, debug=True, reloader=True)
