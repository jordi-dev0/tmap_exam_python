#simple GUI
import sys
from Tkinter import *
import ask_questions_defs as ask
#create the window
filename = "begrippen_volgens_tqc.csv"
mGui = Tk()
ment = StringVar()

v = IntVar()
v.set(1)
res = ask.match_word_gui(filename,"random")
answers = [
    ["Python",1],
    ["Perl",2],
    ["Java",3],
    ["C++",4],
     ]

for ii in range(0,4):
	answers[ii][0] = res[1][ii]

def ShowChoice():
    print v.get()

#modify root window
mGui.title("Simple GUI")
#mGui.geometry("600x500")

question_box = Label(mGui,
      text = res[0],wraplength=500,
      justify = LEFT,
      padx = 20).pack(anchor=W)
rb = []
for txt, val in answers:
	rb.append(Radiobutton (mGui,
                 text=txt,wraplength=500,
                 padx = 20,
                 variable=v,
                 value=val).pack(anchor=W))



mButton = Button(mGui,text ='Submit', command=ShowChoice).pack()

#kick off the event loop
if sys.platform.startswith('win32'):
    mGui.mainloop()

elif sys.platform.startswith('linux'):
    mGui.mainloop()
