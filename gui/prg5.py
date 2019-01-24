# label and button code in oop style

from tkinter import *

class test:
    def __init__(self):
        self.f = Frame(r, height=200, width=500, bg="white")
        self.f.pack()
        self.f.propagate(0)
        self.b1 = Button(self.f, text="click", command=self.handle, width=10, height=2)
        self.b1.pack()

    def handle(self):
        self.l = Label(text="clicked", fg="blue", bg="black")
        self.l.pack()


r = Tk()
a = test()
r.mainloop()