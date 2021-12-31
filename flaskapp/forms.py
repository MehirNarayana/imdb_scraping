from flask_bootstrap import Bootstrap  
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Email, Length



class NumberForm(FlaskForm):
    number = StringField('# on chart', validators=[InputRequired(), Length(max=3)])
    
