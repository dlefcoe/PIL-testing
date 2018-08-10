import time
from tkinter import *
import math


top = Tk()

top.title("moving lines")
top.configure(background = "yellow")

lab1 = Label(top, text = "starting up testing routine", bg = "yellow")

lab1.pack()

# Code to add widgets will go here...
myCan = Canvas(top, bg = "black", height = 400, width = 400)

coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
myCan.pack()
myCan.create_oval(100,100,300,300, fill = "dark blue", outline = "orange", width = 2)
whiteLine = myCan.create_line(200,200,200,150,fill = 'white')
greenLine = myCan.create_line(200,200,250,200,fill = 'green')
someText = myCan.create_text(100,100,  fill = "orange", text="Label text", tag = "tag1")
#top.mainloop()



myCan.delete("tag1")
myCan.create_text(50,50, fill = "red", text = "starting up...", tag = "tag1")
top.update()
time.sleep(1)

for x in range(0,5000):
        myCan.delete(whiteLine)
        myCan.delete(greenLine)

        angle = math.radians(x)

        myCan.delete("tag1")
        myCan.create_text(50,50, fill = "orange", text = "the angle is: "+str(round(angle, 1)), tag = "tag1")


        whiteLine = myCan.create_line(200,200,200+math.cos(angle)*100,200+math.sin(angle)*100,fill = 'white')
        greenLine = myCan.create_line(200,200,200+math.cos(angle/60)*50,200+math.sin(angle/60)*50,fill = 'green')
        top.update()
        time.sleep(0.01)



myCan.delete("tag1")
myCan.create_text(50,50, fill = "yellow", text = "finished now...", tag = "tag1")
top.update()

time.sleep(2)


print('finished')


