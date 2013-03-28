from flask.ext.sqlalchemy import SQLAlchemy
import hashlib


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.password = self._hash_password(kwargs.get("password"))

    def _hash_password(self, password_string):

        """Creates a sha1 hash equivalent of the password"""
        # TODO: This function can be imporved further...
        return hashlib.new('sha1', password_string).hexdigest()
