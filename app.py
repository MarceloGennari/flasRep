from flask import Flask, render_template, request, jsonify
import cognitive_face as CF
import base64
import cognitive_face as CF
from lib import aux_keys
import numpy as np
import pickle
import os
import sys
import pickle
import emoji
from lib.Face import Attribute
from EmojiCreator import emoj
sys.dont_write_bytecode=True

#Setting Cognitive Services
CF.Key.set(aux_keys.KEY)
CF.BaseUrl.set(aux_keys.BASE_URL)
img_url = 'img.jpg'
attributes = (
                'age,gender,headPose,smile,facialHair,glasses,emotion,hair,'
                'makeup,occlusion,accessories,blur,exposure,noise'
)

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

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()

        #Image URL - Local Image or Online Imaged
        result = CF.face.detect(img_url, False, False, attributes=attributes)
        em = emoj(result)
        print(result)
        return jsonify(em)
    else:
        return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True)