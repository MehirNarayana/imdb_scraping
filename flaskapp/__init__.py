from flask import Flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


import flaskapp.routes
