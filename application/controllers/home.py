from flask import Blueprint, render_template, session

from application.models import User


app = Blueprint("home", __name__)


@app.route('')
def index():
    context = {}

    user_id = session.get('user_id', None)

    if user_id:
        user = User.query.get(user_id)
        context['user'] = user

    return render_template('home/index.html', **context)
