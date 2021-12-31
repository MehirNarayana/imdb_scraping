from flask import Flask
from flask import Flask
from flask_bootstrap import Bootstrap  
from flask_wtf import FlaskForm 

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'


import flaskapp.routes