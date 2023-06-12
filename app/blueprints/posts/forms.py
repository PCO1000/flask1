'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CatchForm(FlaskForm):
    img_url = StringField('Image URL', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    ability = StringField('Ability', validators=[DataRequired()])
    base_exp = StringField('Base Experience', validators=[DataRequired])
    submit_btn = SubmitField('Catch')

'''
