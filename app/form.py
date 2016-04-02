from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateImageForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])

