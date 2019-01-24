# assignment question and combo of exp 8 and 10

from tkinter import *
r=Tk()

class subway:
    def __init__(self):

        self.f = Frame(width=200, height=1200, bg="blue")
        self.f.pack()

        self.t = Text(self.f, bg="white")
        self.t.pack(side=LEFT)
        self.bread = ""
        self.s1 = ""
        self.s2 = ""
        self.s3 = ""

        self.cb1v = IntVar()
        self.cb1 = Checkbutton(self.f, text="Mint Mayo", variable=self.cb1v, command=self.dis)
        self.cb1.pack(side=LEFT, padx=10)

        self.cb2v = IntVar()
        self.cb2 = Checkbutton(self.f, text="SOUTH WEST", variable=self.cb2v, command=self.dis)
        self.cb2.pack(side=LEFT, padx=10)

        self.cb3v = IntVar()
        self.cb3 = Checkbutton(self.f, text="SWEET ONION", variable=self.cb3v, command=self.dis)
        self.cb3.pack(side=LEFT, padx=10)

        #this is for radio button same var

        self.rvb = IntVar()

        self.rb1 = Radiobutton(self.f, text="parmesan oregano", variable=self.rvb, value=1)
        self.rb2 = Radiobutton(self.f, text="honey oats", variable=self.rvb, value=2)
        self.rb3 = Radiobutton(self.f, text="italian", variable=self.rvb, value=3)

        self.rb1.pack(side=BOTTOM, pady=10)
        self.rb2.pack(side=BOTTOM, pady=10)
        self.rb3.pack(side=BOTTOM, pady=10)

        self.b1 = Button(self.f,text= "submit", command=self.rad)
        self.b1.place(x=200, y=105)

        self.b = Button(self.f, text="hello", command=self.disp)
        self.b.place(x=200, y=205)

        #self.f.pack()

    def rad(self):
        print(self.rvb.get())

        self.bread = str(self.rvb.get())



    def dis(self):
        if self.cb1v.get():
            self.s3 = "mint mayo"
        if self.cb2v.get():
            self.s2 = "south west"
        if self.cb3v.get():
            self.s1 = "sweet onion"


    def disp(self):
        self.t.insert(1.0,"sauce: "+self.s1+" "+self.s2+" "+self.s3)
        self.t.insert(2.0,"\nbread: "+self.bread)



a = subway()
r.mainloop()


