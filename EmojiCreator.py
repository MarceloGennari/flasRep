import pickle
from lib.Face import Attribute
import sys
sys.dont_write_bytecode=True

# Change this to a new file name for a new image; This is specified in TestCog.py
filename = 'faces/facedetect1'

fileObject = open(filename, 'r')
x = pickle.load(fileObject)

y = x[0]["faceAttributes"]

#print(x)
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

import emoji
if att.emotion == 'neutral':
	print(emoji.emojize(':thumbsup:', use_aliases=True))

if att.emotion == 'happiness':
        print(emoji.emojize(':smile:', use_aliases=True))

if att.emotion == 'sadness':
        print(emoji.emojize(':cry:', use_aliases=True))

if att.emotion == 'anger':
        print(emoji.emojize(':rage:', use_aliases=True))

if att.emotion == 'surprise':
        print(emoji.emojize(':open_mouth:', use_aliases=True))

if att.emotion == 'disgust':
        print(emoji.emojize(':smirk:', use_aliases=True))

if att.emotion == 'fear':
        print(emoji.emojize(':fearful:', use_aliases=True))

if att.emotion == 'contempt':
        print(emoji.emojize(':smirk:', use_aliases=True))
