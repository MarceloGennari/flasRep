import pickle
from lib.Face import Attribute
import sys
sys.dont_write_bytecode=True

filename = 'faces/facedetect'

fileObject = open(filename, 'r')
x = pickle.load(fileObject)

y = x[0]["faceAttributes"]

print(x)
att = Attribute(x[0]["faceAttributes"])
print(att.emotion)

# Possible emotions are:
# neutral
# sadness
# happiness
# disgust
# anger
# surprise
# fear
# contempt

