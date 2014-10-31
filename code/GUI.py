#simple GUI
import sys
from Tkinter import *

#create the window
mGui = Tk()
ment = StringVar()

v = IntVar()
v.set(1)
answers = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
    ]

def ShowChoice():
    print v.get()

#modify root window
mGui.title("Simple GUI")
mGui.geometry("600x500+200+200")

Label(mGui,
      text="Choose your answer",
      justify = LEFT,
      padx = 20).pack()

for txt, val in answers:
    Radiobutton (mGui,
                 text=txt,
                 padx = 20,
                 variable=v,
                 value=val).pack(anchor=W)

mButton = Button(mGui,text ='Submit', command=ShowChoice).pack()

#kick off the event loop
if sys.platform.startswith('win32'):
    mGui.mainloop()

elif sys.platform.startswith('linux'):
    mGui.mainloop()
