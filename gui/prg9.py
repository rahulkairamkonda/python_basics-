# scroll bar for image  try doing it again to understand better

from tkinter import *
r=Tk()

class one:
    def __init__(self):
        self.f = Frame(width=200)
        self.f.pack()
        self.b = Button(self.f, text="hello", command=self.disp)
        self.b.pack()
        self.t = Text(self.f, bg="white")
        self.t.pack(side=LEFT)
        self.name = ""
        self.roll = ""
        self.marks = ""


    def disp(self):
        self.name=input("enter name\n")
        self.roll=input("enter roll\n")
        self.marks=input("enter marks\n")
        self.t.insert(1.0,"name: "+self.name)
        self.t.insert(2.0,"\nroll: "+self.roll)
        self.t.insert(3.0,"\nmarks: "+self.marks)

        self.img = PhotoImage(file='1.png')
        self.t.image_create(END, image=self.img)

        self.s = Scrollbar(r, orient=HORIZONTAL, command=self.t.xview)  # scroll can be given obj like self.t and self.f

        self.s.pack(side=BOTTOM, fill=X)
        self.t.config(xscrollcommand=self.s.set)
        self.s.config(bg="blue")  # not working but not throwing any errors


        self.t.tag_add("1st",'1.0','1.15')
        self.t.tag_add("2nd",'2.0','2.8')
        self.t.tag_add("3rd",'3.0','3.8')  # name of tag, start position , end position

        fnt = ("fore", 18, "bold")
        self.t.tag_config("1st", font=fnt, foreground="black")
        self.t.tag_config("2nd", font=fnt, foreground="blue")
        self.t.tag_config("3rd", font=fnt, foreground="red")

a=one()
r.mainloop()


