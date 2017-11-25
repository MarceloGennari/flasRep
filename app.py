from flask import Flask, render_template, request, jsonify
import base64
import cognitive_face as CF
from lib import aux_keys
# import numpy as np
import os
import sys
from lib.Face import Attribute
from EmojiCreator import emoj
from CarMethods import getattributes, getsleepstate, getPose
#from serial_python_test import MotorSwitch
#import serial

sys.dont_write_bytecode=True

#Setting Cognitive Services
CF.Key.set(aux_keys.KEY)
CF.BaseUrl.set(aux_keys.BASE_URL)
img_url = 'img.jpg'

attributes = getattributes()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method=='POST':

        print("Received")
        image = request.form.get('imgBase64')
        k = request.form.get('scnumb')
        im = 'Data/img'+str(k)+'.jpg'

        print(im)

        f = open(im, 'wb')

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()

        #Image URL - Local Image or Online Imaged
        #result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        if result != []:
            sleepstate = getsleepstate(result)
            pose = getPose(result)

            # if pose["roll"] > 5:
            #     MotorSwitch("ON")
            # if pose["roll"] < -5:
            #     MotorSwitch("OFF")
            
        else:
            print("No face detected")
            sleepstate = "unknown"
            print("No face detected")
        

        return jsonify(sleepstate)

        # em = emoj(result)
        # return jsonify(em)
    else:
        return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=False)