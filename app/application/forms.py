from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name',
                        validators=[DataRequired(message=('Enter a fake name or something.'))])
    email = StringField('Email',
                        validators=[Email(message=('Please enter a valid email address.')),
                                    DataRequired(message=('Please enter a valid email address.'))])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=6, message=('Please select a password with at least 6 characters.')),
                                         EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password',)
    website = StringField('Website',
                          validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter the matching password')])
    submit = SubmitField('Log In')