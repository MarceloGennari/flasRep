from flask import render_template
from app import app

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')