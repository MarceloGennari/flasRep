from flask import render_template, request, jsonify
from app import app
import requests
import cognitive_face as CF
import sys
from lib.usefulutil import getattributes, getsleepstate, getPose, getSleep
import base64
from lib import aux_keys

isArduino = False

# NOTICE: If serial doesn't work, then you have to pip install pyserial, NOT pip install serial!!!!!
if(isArduino):
    from lib.serial_python_test import MotorSwitch
    import serial

img_url = 'img.jpg'

#Setting Cognitive Services
CF.Key.set(aux_keys.KEY)
CF.BaseUrl.set(aux_keys.BASE_URL)
attributes = getattributes()

@app.route('/hardware', methods=['GET', 'POST'])
def hardware():
    if request.method=='POST':
        print("Received")
        image = request.form.get('imgBase64')
        f = open('img.jpg', 'wb')

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()

        #Image URL - Local Image or Online Imaged
        result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        if result != []:
            sleepstate = getsleepstate(result)
            pose = getPose(result)
            roll = pose["roll"]
            print("the roll of the pose is: %d",roll)
            if(isArduino):
                MotorSwitch(roll)

        else:
            print("No face detected")
            sleepstate = "unknown"

        return jsonify(sleepstate)
        # em = emoj(result)
        # return jsonify(em)
    else:
        return render_template('hardware.html')