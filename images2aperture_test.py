import PlotFace
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

eye_list = []

for i in range(0, 51):
    imagefile = '/Users/Bibby/Code/flasRep/data/img%d' % i
    eye_info = PlotFace.ims2aperture(imagefile)
    eye_list.append(eye_info)

# A note on eye_info structure; eye_info = {'leftarea':lefteyearea,'rightarea':righteyearea,'leftlength':lefteyelength,'rightlength':righteyelength}
leftareas = []
rightareas = []
leftlengths = []
rightlengths = []
normalisedleftareas = []

for d in eye_list:
    leftareas.append(d['leftarea'])
    rightareas.append(d['rightareas'])
    leftlengths.append(d['leftlength'])
    rightlengths.append(d['rightlength'])
    normlarea = d['leftarea']/d['leftlength']
    normalisedleftareas.append(normlarea)


plt.plot(normalisedleftareas)

