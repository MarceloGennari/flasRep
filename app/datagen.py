from flask import render_template, request, jsonify
from app import app
import sys
import base64

@app.route('/datagen', methods=['GET','POST'])
def datagen():
    if request.method == 'POST':
        print("Received")
        image = request.form.get('imgBase64')
        nImage = request.form.get('scnumb')
        f = open('data/Dataset2/img2'+str(nImage)+'.jpg', 'wb')

        if sys.version_info[0] == 3:
            bIm = base64.b64decode(bytes(image, 'utf-8'))
        if sys.version_info[0] == 2:
            bIm = base64.b64decode(image)
        f.write(bIm)
        f.close()
       
        return jsonify(True)
    else:
        return render_template('datagen.html')