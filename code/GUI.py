#simple GUI
import sys
from Tkinter import *
import ask_questions_defs as ask
#create the window
filename = "begrippen_volgens_tqc.csv"
question_mode = True
mGui = Tk()
ment = StringVar()

v = IntVar()
v.set(1)
answer= StringVar()
question_text =StringVar()
res = ask.match_word_gui(filename,"random")
answers = [
    ["Python",0],
    ["Perl",1],
    ["Java",2],
    ["C++",3],
     ]

for ii in range(0,4):
	answers[ii][0] = res[1][ii]


	

#modify root window
mGui.title("Simple GUI")
#mGui.geometry("600x500")

question_box = Label(mGui,
      textvariable =question_text ,wraplength=500,
      justify = LEFT,
      padx = 20).pack(anchor=W)
question_text.set(res[0])
rb = []
for txt, val in answers:
	rb.append(Radiobutton (mGui,
                 text=txt,wraplength=500,
                 padx = 20,
                 variable=v,
                 value=val).pack(anchor=W))



answer_box =Label(mGui,textvariable = answer,justify = LEFT, padx = 20).pack(anchor = E)
def ShowChoice(question_mode):
	if question_mode:
		question_mode = False
		if v.get()==res[2]:
			print "bla"
			answer.set("Goed")
		else:
			print "bla"
			answer.set("Fout")
	else:
		question_mode = True
		print "bla"

mButton = Button(mGui,text ='Submit', command=ShowChoice(question_mode)).pack()
#kick off the event loop
if sys.platform.startswith('win32'):
    mGui.mainloop()

elif sys.platform.startswith('linux'):
    mGui.mainloop()
