# list box

from tkinter import *
r=Tk()
r.geometry("400x500+100+100")

class one:
    def __init__(self):
        self.f = Frame(width=800, bg="blue", height=1200)
        self.f.pack()

        self.l1 = Listbox(self.f, height=50, activestyle=DOTBOX, selectmode=MULTIPLE)
        self.l1.pack()
        #pack is needed bind is for the handler

        self.l = ["A", "B", "C", "D"]

        for i in range(len(self.l)):
            self.l1.insert(i,self.l[i])

        self.l1.bind('<<ListboxSelect>>', self.dis)

    def dis(self, event):

        print(self.l1.curselection())

        if(len(self.l1.curselection()))!=0:
            for i in self.l1.curselection():
                print(self.l1.get(i))

a=one()
r.mainloop()


