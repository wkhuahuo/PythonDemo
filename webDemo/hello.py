from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World!<h1>'
    user_agent = request.headers.get('User-Agent')
    meth = request.method
    header = request.headers
    
    return '<p></p><p>Your browser is %s</p><p>method = %s</p><p>headers = %s</p> '% (user_agent,meth, header)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' %name

if __name__ == '__main__':
    app.run(debug=True)