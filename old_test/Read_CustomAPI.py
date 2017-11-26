import pickle
import re

file = '../faces/marcelo'

data = open(file, 'rb')

x = pickle.load(data)
#print(x[["Predictions"]]
y = x.text
a = y.split(",")

tag1 = a[5]
x = tag1.split('"')
print(x[3])

prob1 = a[6]
x = prob1.split('"')
y = re.sub('[^0-9.E-]','', x[2]) #Removing the colon and other possible non numrical things
y = float(y)
print(y)

tag2 = a[8]
x2 = tag2.split('"')
print(x2[3])
prob2 = a[9]
x2 = prob2.split('"')
y2 = re.sub('[^0-9.E-]','', x2[2]) #Removing the colon and other possible non numrical things
y2 = float(y2)
print(y2)

#print(y[0])
#print(x.text)
#print('Done')