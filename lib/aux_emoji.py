import pickle
from lib.aux_face import Attribute
import sys
import emoji
sys.dont_write_bytecode=True

# Change this to a new file name for a new image; This is specified in TestCog.py
#filename = 'faces/facedetect1'

#fileObject = open(filename, 'r')


def emoj(res):
        #x = pickle.load(fileObject)
        x = res

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

        if att.emotion == 'neutral':
                print(emoji.emojize(':thumbsup:', use_aliases=True))
                print(':/')
                return ':/'

        if att.emotion == 'happiness':
                print(emoji.emojize(':smile:', use_aliases=True))
                print(':)')
                return ':)'

        if att.emotion == 'sadness':
                print(emoji.emojize(':cry:', use_aliases=True))
                print(':(')
                return ':('

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


def proc_emo(res):
        x = res
        att = Attribute(x[0]["faceAttributes"])

        # Possible emotions are:
        # neutral
        # sadness
        # happiness
        # disgust
        # anger
        # surprise
        # fear
        # contempt

        if att.emotion == 'neutral':
                print(emoji.emojize(':thumbsup:', use_aliases=True))
                print(':/')
                return 'alright :/'

        if att.emotion == 'happiness':
                print(emoji.emojize(':smile:', use_aliases=True))
                print(':)')
                return 'great! :)'

        if att.emotion == 'sadness':
                print(emoji.emojize(':cry:', use_aliases=True))
                print(':(')
                return 'sad :('

        if att.emotion == 'anger':
                print(emoji.emojize(':rage:', use_aliases=True))
                return 'angry >:('

        if att.emotion == 'surprise':
                print(emoji.emojize(':open_mouth:', use_aliases=True))
                return 'shocked :o'

        if att.emotion == 'disgust':
                print(emoji.emojize(':smirk:', use_aliases=True))
                return 'disgust D:'

        if att.emotion == 'fear':
                print(emoji.emojize(':fearful:', use_aliases=True))
                return 'scared ;-;'
        if att.emotion == 'contempt':
                print(emoji.emojize(':smirk:', use_aliases=True))
                return 'contempt :)'