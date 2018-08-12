def myHello():
    print("hello world")
    print("hello world")
    print("hello world")
    colourList = ["red", "green", "light blue", "orange", "yellow", "pink", "indigo", "violet", "magenta"]

    iMax = 100

    for i in range(0,iMax):
        print("hello jaden " + str(i+1))
        myCan.delete("text01")
        fillCol = random.SystemRandom().choice(colourList)
        ranNum1 = random.randint(1,400)
        ranNum2 = random.randint(1,200)
        loopNum = round((i+1) / iMax * 100,1)
        myCan.create_rectangle(30,40,180,60, fill = "dark red", outline = "dark blue")
        myCan.create_text(100,50,  fill = "white", text="percent complete "+ str(loopNum), tag="text01")
        myCan.create_oval(ranNum1,ranNum2,ranNum1+4,ranNum2+4, fill = fillCol)
        myCan.update()
        #time.sleep(0.01)



myGui = Tk()
myGui.geometry('400x400')
myGui.title("Random Dots Programme")

e1 = Entry(myGui).pack()
#e1.insert(10,"darren")
Label(myGui, text = "press okay to run").pack()
myButton = Button(myGui, text = "ok", command = myHello, fg = "white", bg = "purple").pack()

myCan = Canvas(myGui, width=400, height=200, bg = 'black')
myCan.create_rectangle(30,40,180,60, fill = "dark red", outline = "dark blue")
myCan.create_text(100,50,  fill = "orange", text="starting hello world", tag="text01")
myCan.pack()


myGui.update()
