from flask import render_template, request, jsonify
from app import app
import requests
import sys
import base64
from lib.usefulutil import getSleep
import base64
from lib import aux_keys

CV_KEY = aux_keys.CUSTOM_VISION_KEY
CV_URL = aux_keys.CUSTOM_VISION_URL

@app.route('/sleep', methods=['GET', 'POST'])
def sleep():
    if request.method == 'POST':
        print("Received")
        image = request.form.get('imgBase64')
        f = open('img.jpg', 'wb')

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()

        file = open('img.jpg', 'rb')
        result = requests.post(url=CV_URL,
                            data=file,
                            headers={'Content-Type': 'application/octet-stream',
                                     'Prediction-Key': CV_KEY})

        if result != []:
            sleepstate = getSleep(result)
            print(sleepstate)
        return jsonify(sleepstate)
    else:
        return render_template('sleep.html')