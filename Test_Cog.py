import cognitive_face as CF
from lib import aux_keys
import numpy as np
import pickle
import os
import sys
sys.dont_write_bytecode=True

#Setting Cognitive Services
CF.Key.set(aux_keys.KEY)
CF.BaseUrl.set(aux_keys.BASE_URL)

#Image URL - Local Image or Online Imaged
img_url = 'DSC_0435.JPG'
filename = 'faces/facedetect'
fileObject = open(filename, 'wb')


attributes = (
                'age,gender,headPose,smile,facialHair,glasses,emotion,hair,'
                'makeup,occlusion,accessories,blur,exposure,noise'
)

check = os.path.isfile('filename')

if not check:
    result = CF.face.detect(img_url, False, False, attributes=attributes)
    pickle.dump(result, fileObject)

fileObject.close()
