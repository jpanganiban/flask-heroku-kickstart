from flask import Blueprint, render_template, current_app


app = Blueprint("home", __name__)


@app.route('')
def index():
    return render_template('home/index.html', **{
        'database_config': current_app.config["SQLALCHEMY_DATABASE_URI"],
    })
