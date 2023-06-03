from flask import Flask, request, url_for, render_template, redirect, flash, session
from common import valid_login, log_user_in, if_exsist, create_user

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/terms/')
def terms():
    return render_template('terms.html')

@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif if_exsist:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            create_user(username,password)
            return redirect(url_for('/login'))

        flash(error)

    return render_template('acc/register.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        
        if if_exsist is False:
            error = 'Incorrect username/password'

        if error is None:
            if valid_login(username,password):
                session.clear()
                session['user'] = username
                return redirect(url_for('index'))

        flash(error)
        
    return render_template('acc/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
