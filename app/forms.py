from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class NewForm(FlaskForm):
    description = StringField("Beschreibung", validators=[DataRequired()])
    value = StringField("Original Wert", validators=[DataRequired()])
    submit = SubmitField("Speichern")
