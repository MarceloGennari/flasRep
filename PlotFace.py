import cognitive_face as CF
from lib import aux_keys
import os
import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
sys.dont_write_bytecode=True


def plotface(imagefile):

    #Setting Cognitive Services
    CF.Key.set(aux_keys.KEY)
    CF.BaseUrl.set(aux_keys.BASE_URL)

    #Image URL - Local Image or Online Imaged
    img_url = imagefile

    # only query for the pose attribute, to avoid excessive info/(+delay?)
    attributes = ('headPose')

    check = os.path.isfile('filename')

    if not check:
        result = CF.face.detect(img_url, face_id=False, landmarks=True, attributes=attributes)
        print("total output is %s" % str(result))
        # extract just the first detected face in the image - how can we be sure that this is the driver?
        lm = result[0]["faceLandmarks"]

        # extract all facial features
        i = lm["pupilLeft"]
        n = lm["pupilRight"]
        u = lm["noseTip"]
        v = lm["mouthLeft"]
        y = lm["mouthRight"]
        a = lm["eyebrowLeftOuter"]
        b = lm["eyebrowLeftInner"]
        e = lm["eyeLeftOuter"]
        f = lm["eyeLeftTop"]
        h = lm["eyeLeftBottom"]
        g = lm["eyeLeftInner"]
        c = lm["eyebrowRightInner"]
        d = lm["eyebrowRightOuter"]
        j = lm["eyeRightInner"]
        k = lm["eyeRightTop"]
        m = lm["eyeRightBottom"]
        l = lm["eyeRightOuter"]
        o = lm["noseRootLeft"]
        r = lm["noseRootRight"]
        p = lm["noseLeftAlarTop"]
        s = lm["noseRightAlarTop"]
        q = lm["noseLeftAlarOutTip"]
        t = lm["noseRightAlarOutTip"]
        w = lm["upperLipTop"]
        z = lm["upperLipBottom"]
        aa = lm["underLipTop"]
        ab = lm["underLipBottom"]

        # left eyebrow
        plt.plot([a['x'], b['x']], [a['y'], b['y']], 'b')
        # right eyebrow
        plt.plot([c['x'], d['x']], [c['y'], d['y']], 'b')
        # left eye
        plt.plot([e['x'], f['x'], g['x'], h['x'], e['x']], [e['y'], f['y'], g['y'], h['y'], e['y']], 'b')
        # right eye
        plt.plot([l['x'], k['x'], j['x'], m['x'], l['x']], [l['y'], k['y'], j['y'], m['y'], l['y']], 'b')
        # left nose
        plt.plot([o['x'], p['x'], q['x']], [o['y'], p['y'], q['y']], 'b')
        # right nose
        plt.plot([r['x'], s['x'], t['x']], [r['y'], s['y'], t['y']], 'b')
        # mouth upper
        plt.plot([v['x'], w['x'], y['x'], z['x'], v['x']], [v['y'], w['y'], y['y'], z['y'], v['y']], 'b')
        # mouth lower
        plt.plot([v['x'], aa['x'], y['x'], ab['x'], v['x']], [v['y'], aa['y'], y['y'], ab['y'], v['y']], 'b')
        # nose centre & pupils
        plt.plot([i['x'], n['x'], u['x']], [i['y'], n['y'], u['y']], 'bo')


        plt.axis('equal')
        plt.show()


ii = 4
plotface(imagefile = '/Users/Bibby/Desktop/hackathon_images/sleep%d.jpg' % ii)
plotface()
