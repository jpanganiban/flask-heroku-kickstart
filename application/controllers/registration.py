from flask import (Blueprint, request, render_template, url_for, redirect,
                   session, flash)
from application.models import db, User
from application.forms.registration import RegistrationForm


app = Blueprint('registration', __name__)


@app.route('', methods=['GET', 'POST'])
def index():
    """Registration handler"""

    if request.method == 'GET':
        if session.get('user_id'):
            return redirect(url_for('home.index'))

        form = RegistrationForm()

    if request.method == 'POST':
        if session.get('user_id'):
            return redirect(url_for('home.index'))

        form = RegistrationForm(request.form)
        if form.validate():
            print "VALID"
            user = User(**{
                "email": form.email.data,
                "username": form.username.data,
                "password": form.password.data,
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
            })
            db.session.add(user)
            db.session.commit()

            # Create new session
            session['user_id'] = user.id
            flash("You have successfullly signed-up!")
            return redirect(url_for('home.index'))
        else:
            flash("There was an error in the data you submitted. :(", "error")

    return render_template('registration/index.html', **{
        "form": form
    })
