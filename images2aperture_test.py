import PlotFace
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pickle


filename = 'data/eye_info.txt'
# --- COMMENT FROM HERE TO THE NEXT BIG COMMENT NOW THAT THE FILE IS SAVED ---------

# eye_list = []
#
# for i in range(0, 113):
#     imagefile = '/Users/Bibby/Code/flasRep/data/img%d.jpg' % i
#     eye_info, Face = PlotFace.ims2aperture(imagefile)
#     # Face is a flag that is set to True if a face has been found by the API, False otherwise
#     if Face == True:
#         eye_list.append(eye_info)
#     else:
#         print(i)
#
# fileObject = open(filename, 'wb')
# pickle.dump(eye_list, fileObject)
# fileObject.close()

# ----------------------- START HERE -------------------------------

fileObject = open(filename, 'rb')
eye_list = pickle.load(fileObject)

# A note on eye_info structure; eye_info = {'leftarea':lefteyearea,'rightarea':righteyearea,'leftlength':lefteyelength,'rightlength':righteyelength}
leftareas = []
rightareas = []
leftlengths = []
rightlengths = []
normalisedleftareas = []
normalisedrightareas = []



for d in eye_list:
    leftareas.append(d['leftarea'])
    rightareas.append(d['rightarea'])
    leftlengths.append(d['leftlength'])
    rightlengths.append(d['rightlength'])
    normlarea = d['leftarea']/d['leftlength']
    normrarea = d['rightarea']/d['rightlength']
    normalisedleftareas.append(normlarea)
    normalisedrightareas.append(normrarea)


plt.figure(1)
plt.subplot(311)
plt.title('Normalised left (blue) and right (red) areas')
plt.plot(normalisedleftareas, 'bo')
plt.plot(normalisedrightareas, 'ro')

plt.subplot(312)
plt.title('Normalised left (blue) and right (red) lengths')
plt.plot(leftlengths, 'bo')
plt.plot(rightlengths, 'ro')

plt.subplot(313)
plt.title('Left (blue) and right (red) areas')
plt.plot(leftareas, 'bo')
plt.plot(rightareas, 'ro')
plt.show()
