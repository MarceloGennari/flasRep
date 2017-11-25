from flask import Flask, render_template, request
import cognitive_face as CF
import base64
import os
import io
from PIL import Image
from array import array

"""
KEY = '12e644b9-0a69-4bf0-b923-87523be34460'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print(result)
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video', methods=['POST'])
def video():
    if request.method=='POST':
        print("Received")
        image = request.form.get('imgBase64')
        f = open('img2.jpg', 'wb')
        #bIm = base64.b64encode(bytes(image, 'utf-8'))
        bIm = bytearray(image)
        bImg = Image.open(io.BytesIO(bIm))
        bImg.save('imageTest.jpg')
        f.write(bIm)
        f.close()
        print(request)
        print(bIm)
        return render_template('index.html')
    else:
        return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True)