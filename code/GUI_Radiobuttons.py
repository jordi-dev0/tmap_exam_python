<<<<<<< HEAD
from Tkinter import *

mGui = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print v.get()

Label(mGui, 
      text="""Choose your favourite 
programming language:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(mGui, 
                text=txt,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()
=======
from Tkinter import *

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print v.get()

Label(root, 
      text="""Choose your favourite 
programming language:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, 
                text=txt,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()
>>>>>>> eacb7de20a670b1b0779fdf8a39368c1a3667383
