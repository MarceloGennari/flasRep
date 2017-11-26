import requests
import pickle
from lib import aux_keys

file = 'faces/marcelo'
url = aux_keys.CUSTOM_VISION_URL
data = open('img.jpg', 'rb').read()
res = requests.post(url=url,
                    data=data,
                    headers={'Content-Type': 'application/octet-stream',
                             'Prediction-Key': '32a9268b5e28406baefc060260d9632a'})


fileObject = open(file, 'wb')
pickle.dump(res, fileObject)
fileObject.close()



print(res)
print('Done')
