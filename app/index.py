from flask import render_template
from app import app
import sys
sys.dont_write_bytecode=True

@app.route('/')
def index():
    return render_template('index.html')