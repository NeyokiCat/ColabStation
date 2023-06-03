from flask import Flask, request, url_for, render_template
from common import valid_login, log_user_in
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello"

@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    render_template('login.html', error=error)
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)