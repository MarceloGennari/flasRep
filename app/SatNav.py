from flask import render_template, request, jsonify, Response
from app import app
import requests
import cognitive_face as CF
import sys
from lib.usefulutil import getattributes, getsleepstate, getPose, getSleep
import base64
from lib import aux_keys, aux_speak
import json
from lib.aux_face import Attribute

isArduino = False

# NOTICE: If serial doesn't work, then you have to pip install pyserial, NOT pip install serial!!!!!
if(isArduino):
    from lib.serial_python_test import MotorSwitch
    import serial

img_url = 'app/img.jpg'

#Setting Cognitive Services
CF.Key.set(aux_keys.KEY)
CF.BaseUrl.set(aux_keys.BASE_URL)
attributes = getattributes()

@app.route('/satnav', methods=['GET', 'POST'])
def satnav():
    if request.method=='POST':
        print("Received")
        image = request.form.get('imgBase64')
        f = open(img_url, 'wb')

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()

        #Image URL - Local Image or Online Imaged
        result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        audio = ''
        att = ''
        att = Attribute(result[0]["faceAttributes"])
        if result != []:
            sleepstate = getsleepstate(result)
            pose = getPose(result)
            roll = pose["roll"]
            yaw = pose["yaw"]
            print("the yaw of the pose is: %d",yaw)
            roll_str = str(round(roll,2))
            yaw_str = str(round(yaw, 2))
            yaw_str_name = yaw_str.replace('.','_')
            
            if(abs(yaw)>15):
                audio = 'AudiosAngles/yaw'+str(yaw_str_name)
                aux_speak.converttowav('AudiosAngles/yaw'+str(yaw_str_name), 'You head is at ' + yaw_str + '. Bugger off.' )
            elif(att.emotion == "happiness"):
                audio = 'happy'
                aux_speak.converttowav('happy', 'Why are you so happy? You are ugly, poor and stink' )
            elif(att.emotion =="neutral"):
                audio = 'test1'
            else:
                audio = 'Sad1'
                aux_speak.converttowav('Sad1', 'Don\'t be sad' )

            if(isArduino):
                MotorSwitch(roll)
        else:
            print("No face detected")
            sleepstate = "unknown"

        js = [{"sleep": sleepstate, "roll": roll_str, "yaw": yaw, "emotion": att.emotion, "action": audio}]
        
        return Response(json.dumps(js), mimetype='application/json')
        # return jsonify(em)
    else:
        return render_template('satnav.html')