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
    attributes = ('headPose,occlusion')

    check = os.path.isfile('filename')

    if not check:
        result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        print("total output is %s" % str(result))
        # extract just the first detected face in the image - how can we be sure that this is the driver?
        att = result[0]["faceAttributes"]
        lm = result[0]["faceLandmarks"]
        print(att)
        # extract just the pose from this
        pose = att['headPose']
        eye_occ = att['occlusion']['eyeOccluded']

        # "faceLandmarks": {
        #     "pupilLeft": {
        #         "x": 412.7,
        #         "y": 78.4
        #     },
        #     "pupilRight": {
        #         "x": 446.8,
        #         "y": 74.2
        #     },

        eye_left = lm['pupilLeft']
        eye_right = lm['pupilRight']
        print("left eye co-ords are: x=%f, y=%f" % (eye_left['x'], eye_left['y']))
        print("right eye co-ords are: x=%f, y=%f" % (eye_right['x'], eye_right['y']))
        print("Roll is %f" % pose["roll"])
        print("Yaw is %f" % pose["yaw"])
        print("Eye occlusion: %s" % eye_occ)


    return pose

i = 4
getposefromimage(imagefile = '/Users/Bibby/Desktop/hackathon_images/sleep%d.jpg' % i)
