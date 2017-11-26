from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("img.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("data/arial.ttf", 30)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((120, 80),"I'm Feeling Great!",(255,255,255),font=font)
img.save('sample-out.jpg')