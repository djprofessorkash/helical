"""
FILENAME:               app.py
PROJECT:                HELiCAL
AUTHOR:                 Aakash "Kash" Sudhakar
DESCRIPTION:            Main server setup file for running the HELiCAL project. 
DATE CREATED:           Wednesday, March 20, 2019
DATE LAST MODIFIED:     Wednesday, March 20, 2019
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"