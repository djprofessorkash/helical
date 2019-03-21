"""
FILENAME:               app.py
PROJECT:                HELiCAL
AUTHOR:                 Aakash "Kash" Sudhakar
DESCRIPTION:            Main server setup file for running the HELiCAL project. 
DATE CREATED:           Wednesday, March 20, 2019
DATE LAST MODIFIED:     Wednesday, March 20, 2019
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def user_form():
    return render_template("input-data.html")

@app.route("/", methods=["POST"])
def user_form_POST():
    text = request.form["text"]
    return "Your input is {}. How quaint!".format(text.upper())