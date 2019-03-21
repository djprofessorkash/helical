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
from .structures import processor01, processor02, processor03

# Initializes Flask App
app = Flask(__name__)

# Creates Home Page with User Data Input Option
@app.route("/")
def user_form():
    return render_template("input-data.html")

# Creates POST Route at Home Page with User Data Processing
@app.route("/", methods=["POST"])
def user_form_proc():
    # NOTE: PROCESSORS values reflect the _value_ tags in the HTML button elements in ./templates/input-data.html.
    PROCESSORS = {
        1: "Get Nucleotide Count",
        2: "Convert to RNA",
        3: "Generate Reverse Complement"
    }
    if request.form["proc"] == PROCESSORS[1]:
        if request.form["proc01"]:
            text01 = request.form["proc01"].upper()
            proc01 = processor01.Processor01_NucleotideCounter(text01)
            return proc01.render_response(proc01.nucleotide_counter())
        else:
            return "ERROR: Nucleotide Counts Processor did not receive any data."
    elif request.form["proc"] == PROCESSORS[2]:
        if request.form["proc02"]:
            text02 = request.form["proc02"].upper()
            proc02 = processor02.Processor02_DNATransriber(text02)
            return proc02.render_response(proc02.transcriber())
        else:
            return "ERROR: RNA Transcriber Processor did not receive any data."
    elif request.form["proc"] == PROCESSORS[3]:
        if request.form["proc03"]:
            text03 = request.form["proc03"].upper()
            proc03 = processor03.Processor03_ReverseComplement(text03)
            return proc03.render_response(proc03.reverse_complement_generator())
        else:
            return "ERROR: Reverse Complement Processor did not receive any data."
    # elif request.form["proc"] == PROCESSORS[4]:
    #     if request.form["proc04"]:
    #         # process 4
    #         pass
    #     else:
    #         return "ERROR: ..."
    # elif request.form["proc"] == PROCESSORS[5]:
    #     if request.form["proc05"]:
    #         # process 5
    #         pass
    #     else:
    #         return "ERROR: ..."
