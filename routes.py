from flask import render_template
from app import app
from templates import *


@app.route('/')
def home():
    return render_template('index.html')