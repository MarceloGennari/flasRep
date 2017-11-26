from flask import render_template, request, jsonify
from app import app

import base64
import cognitive_face as CF
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from lib.usefulutil import getattributes, getsleepstate, getPose, getSleep
from lib import aux_keys, aux_emoji

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

@app.route('/video', methods=['GET', 'POST'])
def video():
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
        result = CF.face.detect(img_url, face_id=False, landmarks=False, attributes=attributes)
        if result != []:
            x = aux_emoji.proc_emo(result)
            img = Image.open("img.jpg")
            draw = ImageDraw.Draw(img)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("data/arial.ttf", 30)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((120, 80), "I'm Feeling " + x, (255, 255, 255), font=font)
            img.save('app/static/sample-out.jpg')
            print(result)
        else:
            print("No face detected")
        return jsonify(result)
    else:
        return render_template('video.html')





