#Cut down version from the SDK example

import operator

def key_with_max_value(item):
    """Get the key with maximum value in a dict."""
    return max(item.items(), key=operator.itemgetter(1))[0]

class Attribute(object):
    """Attributes for face."""
    def __init__(self, attr):
        super(Attribute, self).__init__()
        self.set_attr(attr)

    def set_attr(self, attr):
        """Set the attribute value."""
        self.gender = attr['gender']
        self.age = int(attr['age'])
        if not attr['hair']['hairColor']:
            if attr['hair']['invisible']:
                self.hair = 'Invisible'
            else:
                self.hair = 'Bald'
        else:
            self.hair = max(
                attr['hair']['hairColor'],
                key=lambda x: x['confidence']
            )['color']
        self.facial_hair = sum(attr['facialHair'].values()) > 0 and 'Yes' \
            or 'No'
        self.makeup = any(attr['makeup'].values())
        self.emotion = key_with_max_value(attr['emotion'])
        self.occlusion = any(attr['occlusion'].values())
        self.exposure = attr['exposure']['exposureLevel']
        self.head_pose = "Pitch: {}, Roll:{}, Yaw:{}".format(
            attr['headPose']['pitch'],
            attr['headPose']['roll'],
            attr['headPose']['yaw']
        )
        if not attr['accessories']:
            self.accessories = 'NoAccessories'
        else:
            self.accessories = ' '.join(
                [str(x['type']) for x in attr['accessories']]
            )