# insert the value and display it in the text box

'''
for radio button the variable should be only one not 3 like in the eg below
'''

from tkinter import *
r=Tk()

class subway:
    def __init__(self):

        self.f = Frame(width=200)
        self.f.pack()

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


        self.b = Button(self.f,text= "submit", command=self.rad)
        #self.b.pack(side=BOTTOM, pady=10)
        self.b.place(x=200, y=105)

    def rad(self):
        print(self.rvb.get())




    def dis(self):
        if self.cb1v.get():
            print("mint mayo")
        if self.cb2v.get():
            print("south west")
        if self.cb3v.get():
            print("sweet onion")



a=subway()
r.mainloop()


