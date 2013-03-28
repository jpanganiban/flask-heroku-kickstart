from flask import Flask, session
from flask.ext.heroku import Heroku
from flask.ext.bootstrap import Bootstrap

from application.models import db
from application.controllers import home, registration, authentication


def has_session():
    """Returns true if there's an existing user session"""
    return bool(session.get('user_id', None))


def create_app(config=None):
    """Our application factory. It optionally takes a config
    object that can be used to update our applications
    configuration"""

    app = Flask(__name__, template_folder='views')

    if config:
        app.config.from_object(config)

    # Install plugins after the comment
    heroku = Heroku(app)
    bootstrap = Bootstrap(app)
    db.init_app(app)

    # Install blueprints after the comment
    app.register_blueprint(home.app, url_prefix="/")
    app.register_blueprint(registration.app, url_prefix="/registration")
    app.register_blueprint(authentication.app, url_prefix="/auth")

    # Some jinja helpers

    app.jinja_env.globals.update(has_session=has_session)

    return app
