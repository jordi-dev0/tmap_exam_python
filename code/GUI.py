#simple GUI
import sys
from Tkinter import *

def tekst():
    mtext = ment.get()
    mlabel2 = Label(mGui,text=mtext).grid(row=2,column=0,sticky=W)

#create the window
mGui = Tk()
ment = StringVar()

#modify root window
mGui.title("Simple GUI")
mGui.geometry("600x500+200+200")

mEntry = Entry(mGui,textvariable=ment).grid(row=0,column=0,sticky=W)

mButton = Button(mGui,text ='Ok', command = tekst,).grid(row=0,column=1)


#kick off the event loop
if sys.platform.startswith('win32'):
    mGui.mainloop()

elif sys.platform.startswith('linux'):
    print (linux)

