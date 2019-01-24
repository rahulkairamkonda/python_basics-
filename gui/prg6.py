from tkinter import *
class test:
    def __init__(self):
        self.f = Frame(r, height=200, width=500, bg="white")
        self.f.pack()
        self.f.propagate(0)
        self.b1 = Button(self.f, text="blue", command=lambda: self.handle(1), width=10, height=2)   # to pass a parameter lambda is needed
        self.b1.pack()
        self.b2 = Button(self.f, text="red", command=lambda: self.handle(2), width=10, height=2)
        self.b2.pack()
        self.l = Label(self.f, text="clicked", fg="black")
        self.l.pack()

    def handle(self, c):
        if c == 1:
            self.l.config(text="blue is clicked")
        else:
            self.l.config(text="red is clicked")    # self.l["text"]="test" or["bg"]="red"

# you can add the label inside the def handle so that we can print label multiple times 


r = Tk()
a = test()
r.mainloop()