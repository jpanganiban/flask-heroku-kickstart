from flask import Blueprint, render_template


app = Blueprint("home", __name__)


@app.route('')
def index():
    return render_template('home/index.html')
