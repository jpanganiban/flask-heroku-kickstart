from flask import (Blueprint, session, redirect, url_for, request,
                   render_template)

from application.forms.authentication import LoginForm
from application.models import User


app = Blueprint('authentication', __name__)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home.index'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.form)

        if form.validate():
            # TODO: We can just abstract this in the User.authenticate
            # method.
            session['user_id'] = User.query.\
                filter_by(username=form.username.data).first().id
            return redirect(url_for('home.index'))

    return render_template('authentication/login.html', **{
        "form": form
    })
