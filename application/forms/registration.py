from flask.ext import wtf
from application.models import User


class RegistrationForm(wtf.Form):
    """Our registration form"""
    username = wtf.TextField("Username", validators=[wtf.Required()])
    password = wtf.PasswordField("Password", validators=[wtf.Required()])
    email = wtf.TextField("Email", validators=[wtf.Email()])
    first_name = wtf.TextField("First Name")
    last_name = wtf.TextField("Last Name")

    def validate_username(form, field):
        if User.query.filter_by(username=field.data).first():
            raise wtf.ValidationError("Username taken!")

    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first():
            raise wtf.ValidationError("Email taken!")
