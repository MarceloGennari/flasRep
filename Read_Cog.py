import pickle
from lib.Face import Attribute

filename = 'faces/facessleeping'

fileObject = open(filename, 'rb')
x = pickle.load(fileObject)

# extract just the first detected face in the image - how can we be sure that this is the driver?
y = x[0]["faceAttributes"]
# print("y is %s" % y)

# print("x is %s" % x)
att = Attribute(x[0]["faceAttributes"])
print(att.head_pose)


# Possible emotions are:
# neutral
# sadness
# happiness
# disgust
# anger
# surprise
# fear
# contempt

