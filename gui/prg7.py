from tkinter import *
r=Tk()
class stud:

    def __init__(self,a,b,c):
        self.f = Frame(r, height=200, width=500, bg="white")
        self.f.pack()
        self.f.propagate(0)
        self.m = Message(self.f, text="name is:"+a+"\nage is:"+b+"\nroll is:"+c, fg="black", width=200)   # diff between label and message is in smaller width new text goes to next line
        self.m.pack()




print("enter details")
name = input("enter name")
age = input("enter age")
roll = input("enter roll no")

a=stud(name,age,roll)
r.mainloop()


# messages is used for paragraphs of text
# depends on the width when the line is fit into the width it moves to next line unlike label


# ***   can gvie a button in init with def display to ask values from user and command=self.disp
# note def dis takes values from user as input

