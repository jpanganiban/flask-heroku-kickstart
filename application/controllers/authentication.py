from flask import Blueprint, session, redirect, url_for


app = Blueprint('authentication', __name__)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home.index'))


@app.route('login')
def login():
    pass
