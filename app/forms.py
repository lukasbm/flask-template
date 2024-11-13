from wtforms import StringField, SubmitField, SelectField, MultipleFileField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Optional, length
from flask_wtf import FlaskForm


class User(FlaskForm):
    name = StringField('Name', validators=[Required(), length(max=64)])
    submit = SubmitField('Hochladen')
