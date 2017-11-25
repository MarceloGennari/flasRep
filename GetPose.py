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

    # only query for the pose attribute, to avoid excessive info/(+delay?)
    attributes = ('headPose')

    check = os.path.isfile('filename')

    if not check:
        result = CF.face.detect(img_url, False, False, attributes=attributes)
        print(result)
        # extract just the first detected face in the image - how can we be sure that this is the driver?
        y = result[0]["faceAttributes"]
        # extract just the pose from this
        pose = {"Pitch": y['headPose']['pitch'], "Roll": y['headPose']['roll'], "Yaw": y['headPose']['yaw']}
        print("Roll is %d" % pose["Roll"])

    return pose

i = 1
getposefromimage(imagefile = '/Users/Bibby/Desktop/hackathon_images/sleep%d.jpg' % i)
