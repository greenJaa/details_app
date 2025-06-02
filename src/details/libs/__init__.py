#from details.libs import libs

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class connectionForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Submit = SubmitField('Submit')