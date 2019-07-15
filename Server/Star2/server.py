import json
from random import randrange
from bottle import route, run,static_file,request

names = [
{"name": "yosi", "age": "15"},
{"name": "moshe", "age": "8"},
{"name": "eli", "age": "30"},
{"name": "momo", "age": "40"}
]
@route('/')
def hello():
    my_rnd=randrange(4)
    return json.dumps(names[my_rnd])

run(host='localhost', port=7000, debug=True,reloader=True)

if __name__ == '__main__':
    main()