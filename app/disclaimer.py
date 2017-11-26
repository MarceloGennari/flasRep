from flask import render_template
from app import app

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')