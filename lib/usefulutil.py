import re

def getattributes():
    attributes = ('age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise')
    return attributes

def getsleepstate(res):
    att = res[0]["faceAttributes"]
    lm = res[0]["faceLandmarks"]
    # extract just relevant things from this
    pose = att['headPose']
    print("Roll is %f" % pose["roll"])
    print("Yaw is %f" % pose["yaw"])
    if pose["roll"] > 8 or pose["yaw"] > 10:
        sleepstate = "asleep"
        print("YOU ARE ASLEEP - WAKE UP!")
    else:
        sleepstate = "awake"
        print("You are probably awake...")
    return sleepstate

def getPose(res):
    att = res[0]["faceAttributes"]
    lm = res[0]["faceLandmarks"]
    # extract just relevant things from this
    pose = att['headPose']
    return pose

def getSleep(x):
    # Splitting up the string
    y = x.text
    a = y.split(",")
    # Extracting the first tag (from classifier)
    tag1 = a[5]
    x1 = tag1.split('"')
    state1 = x1[3]

    #Extracing the probability
    prob1 = a[6]
    x = prob1.split('"')
    y = re.sub('[^0-9.E-]','', x[2]) #Removing the colon and other possible non numrical things
    state1_prob = float(y)

    # Extracting the second tag (from classifier)
    tag2 = a[8]
    x2 = tag2.split('"')
    state2 = x2[3]

    # Extracing the probability of the second tag
    prob2 = a[9]
    x = prob2.split('"')
    y = re.sub('[^0-9.E-]','', x[2]) #Removing the colon and other possible non numrical things
    state2_prob = float(y)

    if state1_prob > state2_prob:
        return state1
    else:
        return state2