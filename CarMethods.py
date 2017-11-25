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
    if pose["roll"] > 4 or pose["yaw"] > 4:
        sleepstate = "asleep"
        print("YOU ARE ASLEEP - WAKE UP!")
    else:
        sleepstate = "awake"
        print("You are probably awake...")
    return sleepstate