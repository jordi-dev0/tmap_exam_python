#simple GUI
import sys
from Tkinter import *
import ask_questions_defs as ask
#create the window
filename = "begrippen_volgens_tqc.csv"
mGui = Tk()
ment = StringVar()

v = IntVar()
b_text =StringVar()
b_text.set("Submit")
answer= StringVar()
question_text =StringVar()
a1 = StringVar()
a2 = StringVar()
a3 = StringVar()
a4  =StringVar()
res = ask.match_word_gui(filename,"random")
answers = [
    [a1,0],
    [a2,1],
    [a3,2],
    [a4,3],
     ]

for ii in range(0,4):
	answers[ii][0].set(res[1][ii])


	

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
                 textvariable=txt,wraplength=500,
                 padx = 20,
                 variable=v,
                 value=val,justify=LEFT).pack(anchor=W))

def change_res(r):
	res = r


answer_box =Label(mGui,textvariable = answer,justify = LEFT, padx = 20).pack(anchor = E)
def ShowChoice():
	if b_text.get()=="Submit":
		if v.get()==res[2]:
			answer.set("Goed")
		else:
			answer.set("Fout")
		b_text.set("Next")
	else:
		b_text.set("Submit")
		answer.set("")
		res0 = ask.match_word_gui(filename,"random")
		for ii in range(0,4):
			answers[ii][0].set(res0[1][ii])
		question_text.set(res0[0])
		change_res(res0)
 
mButton = Button(mGui,textvariable =b_text, command=ShowChoice).pack()
#kick off the event loop
if sys.platform.startswith('win32'):
    mGui.mainloop()

elif sys.platform.startswith('linux'):
    mGui.mainloop()
