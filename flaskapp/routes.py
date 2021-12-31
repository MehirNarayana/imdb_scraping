from __future__ import print_function
from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flaskapp.scraping_script import all_movies
from flaskapp.forms import *
from flaskapp import app
import re
import json



@app.route("/index", methods=["POST", "GET"])
def index():



    form = NumberForm()


    if request.method == "POST":

        get_data = request.form['number']

        number = int(get_data)
        query = re.compile(r'\s*(\d+\.)\s+(.*)\s+(\(\d+\))')
        formatted_result = query.search(all_movies[number-1])
        number_result = formatted_result.group(1)
        name = formatted_result.group(2)
        date = formatted_result.group(3)

        return jsonify({number_result: number_result})

    else:
        return render_template('index.html', templates='templates', form=form)
