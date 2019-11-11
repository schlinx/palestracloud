#! -*- coding: utf8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Say good bye brow!"
