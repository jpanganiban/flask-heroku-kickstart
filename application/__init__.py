from flask import Flask
from flask.ext.heroku import Heroku

from application.models import db
from application.controllers import home


def create_app(config=None):
    """Our application factory. It optionally takes a config
    object that can be used to update our applications
    configuration"""

    app = Flask(__name__, template_folder='views')

    if config:
        app.config.from_object(config)

    # Install plugins after the comment
    db.init_app(app)
    heroku = Heroku(app)

    # Install blueprints after the comment
    app.register_blueprint(home.app, url_prefix="/")

    return app
