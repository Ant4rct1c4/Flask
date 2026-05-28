from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp


class ContactForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(min=4, max=10)
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    phone = StringField(
        'Phone',
        validators=[
            DataRequired(),
            Regexp(r'^\+380\d{9}$', message='Phone must be like +380XXXXXXXXX')
        ]
    )

    subject = SelectField(
        'Subject',
        choices=[
            ('question', 'Question'),
            ('support', 'Support'),
            ('offer', 'Offer')
        ],
        validators=[
            DataRequired()
        ]
    )

    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(),
            Length(max=500)
        ]
    )

    submit = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField(
        'Username / Email',
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=4, max=10)
        ]
    )

    remember = BooleanField('Remember me')

    submit = SubmitField('Sign in')