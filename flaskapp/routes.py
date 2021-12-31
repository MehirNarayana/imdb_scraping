from __future__ import print_function
from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

from flaskapp.forms import *
from flaskapp import app
from flaskapp.scraping_script import Script
import re
import json



@app.route("/", methods=["POST", "GET"])
def index():



    form = NumberForm()


    if request.method == "POST":

        get_data = request.form['number']

        number = int(get_data)

        obj = Script(number)
        obj.find_element()
        get = obj.get_movie()
        number_result = get[0]
        name = get[1]
        date = get[2]





        return render_template('index.html', templates='templates', form=form, number_result=number_result, name=name, date=date)

    else:
        return render_template('index.html', templates='templates', form=form, number_result='', name='', date='')
