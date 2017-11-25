import pickle
from lib.Face import Attribute

filename = 'faces/facedetect'

fileObject = open(filename, 'rb')
x = pickle.load(fileObject)

# extract just the first detected face in the image - how can we be sure that this is the driver?
y = x[0]["faceAttributes"]

# print("y is %s" % y)

Pose = {"Pitch":y['headPose']['pitch'],"Roll":y['headPose']['roll'],"Yaw":y['headPose']['yaw']}
print(Pose["Pitch"])
print(Pose["Roll"])
print(Pose)
# print(pitch)

#
# self.head_pose = "Pitch: {}, Roll:{}, Yaw:{}".format(
#             attr['headPose']['pitch'],
#             attr['headPose']['roll'],
#             attr['headPose']['yaw']
#         )

# att = Attribute(y)
