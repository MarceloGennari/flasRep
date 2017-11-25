import cognitive_face as CF
from lib import aux_keys
import pickle
import os
import sys
sys.dont_write_bytecode=True


def getposefromimage(imagefile):

    #Setting Cognitive Services
    CF.Key.set(aux_keys.KEY)
    CF.BaseUrl.set(aux_keys.BASE_URL)

    #Image URL - Local Image or Online Imaged
    img_url = imagefile
    filename = 'faces/facessleeping'
    fileObject = open(filename, 'wb')


    attributes = (
                    'headPose'
    )

    check = os.path.isfile('filename')

    if not check:
        result = CF.face.detect(img_url, False, False, attributes=attributes)
        print(result)
        y = x[0]["faceAttributes"]
        print("y is %s" % s)
        pickle.dump(result, fileObject)

    fileObject.close()

    from lib.Face import Attribute


def getpose(filename):
    fileObject = open(filename, 'rb')
    x = pickle.load(fileObject)

    # extract just the first detected face in the image - how can we be sure that this is the driver?
    y = x[0]["faceAttributes"]

    pose = {"Pitch":y['headPose']['pitch'],"Roll":y['headPose']['roll'],"Yaw":y['headPose']['yaw']}
    print(pose["Pitch"])

    return pose


getposefromimage(imagefile = '/Users/Bibby/Desktop/hackathon_images/sleep1.jpg')
Pose = getpose(filename = 'faces/facessleeping')

print(Pose)
