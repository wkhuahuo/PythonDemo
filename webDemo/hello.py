from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World!<h1>'
    # user_agent = request.headers.get('User-Agent')
    # meth = request.method
    # header = request.headers
    
    # return '<p></p><p>Your browser is %s</p><p>method = %s</p><p>headers = %s</p> '% (user_agent,meth, header)

    return '<h1>Bad Request</h1>',400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

    # return redirect('https://www.baidu.com')


@app.route('/reds')
def reds():
    return redirect('https://www.baidu.com')


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s</h1>' %name

@app.route('/user/<id>')
def get_user(id):
    u = True
    if not u:
        abort(404)
    return '<h1>Hello num , %s</h1>' % id


if __name__ == '__main__':
    app.run(debug=True)