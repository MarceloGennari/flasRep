from flask import render_template
from app import app

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')