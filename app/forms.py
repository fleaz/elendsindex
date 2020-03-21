from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class NewForm(FlaskForm):
    description = StringField("Decription", validators=[DataRequired()])
    value = StringField("Original Value", validators=[DataRequired()])
    submit = SubmitField("Submit")
