# spin box

from tkinter import *
r=Tk()

class one:
    def __init__(self):

        self.f = Frame(width=200)
        self.f.pack()

        self.sp = IntVar()
        self.sp = Spinbox(self.f,from_=0, to=10, textvariable=self.sp)
        self.sp.pack()

        self.sp1 = StringVar()
        self.val = ["A", "B", "C"]
        self.sp1 = Spinbox(self.f,values=self.val, textvariable=self.sp1)
        self.sp1.pack()

        self.b = Button(self.f, text="print the above val", command=self.disp)
        self.b.pack()

    def disp(self):

        print(self.sp.get())
        print(self.sp1.get())

a=one()
r.mainloop()


