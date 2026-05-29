from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    DateTimeLocalField,
    SelectField,
    SubmitField
)
from wtforms.validators import DataRequired, Length
from datetime import datetime


class PostForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Length(min=3, max=150)
        ]
    )

    content = TextAreaField(
        'Content',
        validators=[
            DataRequired(),
            Length(min=5)
        ]
    )

    is_active = BooleanField(
        'Active post',
        default=True
    )

    publish_date = DateTimeLocalField(
        'Publish Date',
        format='%Y-%m-%dT%H:%M',
        default=datetime.utcnow,
        validators=[
            DataRequired()
        ]
    )

    category = SelectField(
        'Category',
        choices=[
            ('news', 'News'),
            ('publication', 'Publication'),
            ('tech', 'Tech'),
            ('other', 'Other')
        ],
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Save Post')