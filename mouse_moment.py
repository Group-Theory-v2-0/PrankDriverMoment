import tkinter
import mouse, time
from datetime import datetime, timedelta
import random
from screeninfo import get_monitors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from telnetlib import NOP
import kbedit

def hookCallback(mouseEvent):
    if (type(mouseEvent) == mouse.MoveEvent):
        print(mouseEvent.y / screenHeight)
        print(mouseEvent.x / screenWidth)
        #saySomeStupidGarbageBecausePythonSucksAndIHateItSoMuchAllTheTime()
    if (type(mouseEvent) == mouse.WheelEvent):
        print(mouseEvent)
    if (type(mouseEvent) == mouse.ButtonEvent):
        print(mouseEvent)
        if(mouseEvent.event_type == mouse.DOWN):
            #print(isPaused)
            global isPaused
            isPaused = False
            print(isPaused)


isPaused = False
screenWidth = get_monitors()[0].width
screenHeight = get_monitors()[0].height

root = Tk()
root.geometry("200x200")
root.overrideredirect(True)

#textWindow = Tk()
#textWindow.geometry("400x50")
#textWindow.overrideredirect(True)
msgroot = Tk()
msgroot.geometry("300x300")
#msg = Message(msgroot, text="Howdy, partner")
#msg.pack()
msgroot.withdraw()
windowX = 2
windowY = 2

reetikPicLeft = ImageTk.PhotoImage(Image.open("ReetikLeft.jpg"))
reetikPicRight = ImageTk.PhotoImage(Image.open("ReetikRight.jpg"))
reetikPicCenter = ImageTk.PhotoImage(Image.open("ReetikCenter.jpg"))
panel = tkinter.Label(root, image = reetikPicLeft)
panel.pack(side = "right", fill = "both", expand = "yes")

def saySomeStupidGarbageBecausePythonSucksAndIHateItSoMuchAllTheTime():
    root.withdraw()
    messagebox.showinfo("Howdy, partner", "HOWDY!")

def getEvents():
    iteration = datetime.now()
    global isPaused
    isPaused = False
    global windowX
    global windowY
    global panel
    count = 0 
    mouse.hook(hookCallback)
    reetikSetting = 0
    dx = 0.05
    dy = 0.02
    while(1): 
        root.geometry("+" + str(int(windowX)) + "+" + str(int(windowY)))
        root.attributes("-topmost", True)
        windowX = (windowX)%screenWidth
        windowY = windowY%screenHeight
        dt = datetime.now() - iteration
        #print(count)
        if(count >= 10000 and count < 12500):
            isPaused = True
        if(count >= 30000 and count < 32500):
            isPaused = True

        if(not isPaused):
            windowX+=dx
            windowY+=dy
            if (windowX >= screenWidth-400):
                dx = -(random.randrange(0, 50, 1) / 100)
                panel.configure(image=reetikPicRight)
                reetikSetting = True
                #isPaused = True
            elif (windowX <= 1):
                dx = (random.randrange(0, 50, 1) / 100)
                panel.configure(image=reetikPicLeft)
                reetikSetting = False
            if (windowY >= screenHeight-400):
                dy = -(random.randrange(0, 50, 1) / 100)
            elif (windowY <= 1):
                dy = (random.randrange(0, 50, 1) / 100)
        elif((dt > timedelta(seconds=1)) or isPaused):
            panel.configure(image=reetikPicCenter)
            msgroot.geometry("+"+str(int((screenWidth/2)-200)) + "+" + str(int((screenHeight/2)-200)))
            if(count >= 10000 and count < 10100):
                msg = Message(msgroot, text="Let me help you out here...")
                kbedit.google_search_removal()
                isPaused = False
            if(count >= 30000 and count < 30100):
                msg = Message(msgroot, text = "Ok, let's play a game. Click keys to beat minesweeper")
                kbedit.minesweep_keys
                isPaused = False
            msg.pack()
            msgroot.deiconify()
            msgroot.update()
            while(isPaused):
                NOP
            if(reetikSetting):
                panel.configure(image=reetikPicRight)
            else:
                panel.configure(image=reetikPicLeft)
            msgroot.withdraw()
            msg.destroy()
            msgroot.update()
            iteration = datetime.now()
            
        #print(windowX)
        #time.sleep(5)
        count +=1
        root.update()
        #textWindow.update()

root.after(10, getEvents)
root.mainloop()