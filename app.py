from flask import Flask, render_template, request, jsonify
import base64
import cognitive_face as CF
from lib import aux_keys
# import numpy as np
import os
import sys
from lib.Face import Attribute
from EmojiCreator import emoj
from CarMethods import getattributes, getsleepstate
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
        f = open('img.jpg', 'wb')
        bIm = base64.b64decode(bytes(image, 'utf-8'))
        f.write(bIm)
        f.close()

        #Image URL - Local Image or Online Imaged
        result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        if result != []:
            sleepstate = getsleepstate(result)
            print("No face detected")
        else:
            sleepstate = "unknown"
        return jsonify(sleepstate)
        # em = emoj(result)
        # return jsonify(em)
    else:
        return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=False)