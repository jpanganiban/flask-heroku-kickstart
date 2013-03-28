from flask.ext import wtf
from application.models import User


class LoginForm(wtf.Form):
    """Our login form"""
    username = wtf.TextField("Username", validators=[wtf.Required()])
    password = wtf.PasswordField("Password", validators=[wtf.Required()])

    def validate_username(form, field):
        if not User.query.filter_by(username=field.data).first():
            raise wtf.ValidationError("Username does not exist")

    def validate_password(form, field):
        if not User.authenticate(form.username.data, form.password.data):
            raise wtf.ValidationError("Failed to authenticate")
