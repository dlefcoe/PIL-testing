import time
from tkinter import *

top = Tk()

top.title("moving lines")
top.configure(background = "yellow")

lab1 = Label(top, text = "starting up testing routine", bg = "yellow")

lab1.pack()

# Code to add widgets will go here...
myCan = Canvas(top, bg = "black", height = 250, width = 400)

coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
myCan.pack()
whiteLine = myCan.create_line(10,10,50,50,fill = 'white')
greenLine = myCan.create_line(10,10,5,25,fill = 'green')
someText = myCan.create_text(100,100,  fill = "orange", text="Label text", tag = "tag1")
#top.mainloop()


for rot in range(0,3):
    myCan.delete("tag1")
    loopString = "loop number: " + str(rot+1)
    myCan.create_text(100,100, fill = "yellow", text = loopString, tag = "tag1")
    for x in range(0,100):
        myCan.move(whiteLine, 2, 0) # move right
        top.update()
        time.sleep(0.01)

    for x in range(0,100):
        myCan.move(whiteLine, 0, 2) # move down
        top.update()
        time.sleep(0.01)

    for x in range(0,100): 
        myCan.move(whiteLine, -2, 0) # move left
        top.update()
        time.sleep(0.01)

    for x in range(0,100):
        myCan.move(whiteLine, 0, -2) #move up
        top.update()
        time.sleep(0.01)

    for x in range(0,100):
        myCan.move(greenLine, 2, 0) # move right
        top.update()
        time.sleep(0.01)

    for x in range(0,100):
        myCan.move(greenLine, 0, 2) # move down
        top.update()
        time.sleep(0.01)

    for x in range(0,100): 
        myCan.move(greenLine, -2, 0) # move left
        top.update()
        time.sleep(0.01)

    for x in range(0,100):
        myCan.move(greenLine, 0, -2) #move up
        top.update()
        time.sleep(0.01)

time.sleep(1)


print('finished')


