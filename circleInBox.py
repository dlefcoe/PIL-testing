from PIL import Image
import os

curDir = os.getcwd()
fileName = 'imageCircle.png'
fn = curDir + "\\" + fileName


im = Image.open(fn)
#im.show()
im.save('F:\programming\python\python tutorial 6 - circle in a box\imageCircle.jpg')
im.save(curDir + "\\" +'another.jpg')

for f in os.listdir('.'):
    print(f)


#draw = ImageDraw.Draw(im)
#draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,255))
