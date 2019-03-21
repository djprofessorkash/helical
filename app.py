"""
FILENAME:               app.py (/helical-project/)
PROJECT:                HELiCAL
AUTHOR:                 Aakash "Kash" Sudhakar
DESCRIPTION:            Main server setup file for running the HELiCAL project. 
DATE CREATED:           Wednesday, March 20, 2019
DATE LAST MODIFIED:     Wednesday, March 20, 2019
"""

# Imports Essential Assets from Flask
from flask import Flask, request, render_template

# Imports Custom Algorithm Structures for Data Processing
# from .structures import processor01
from .structures import processor01

# Initializes Flask App
app = Flask(__name__)

# Creates Home Page with User Data Input Option
@app.route("/")
def user_form():
    return render_template("input-data.html")

# Creates POST Route at Home Page with User Data Processing
@app.route("/", methods=["POST"])
def user_form_POST():
    text = request.form["proc01"]
    proc01 = processor01.Processor01_NucleotideCounter(text)
    return proc01.render_response(proc01.nucleotide_counter())