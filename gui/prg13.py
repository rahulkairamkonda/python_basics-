'''
the below code is for login page
with user and password and a login buttton

later try displaying user name in the same page using msg box or label by doing self.["label"](something like that)
'''

from tkinter import *
r=Tk()
r.geometry("1200x800+100+100")

class one:
    def __init__(self):
        self.f = Frame(width=800, bg="blue", height=1200)    # height and width is not default coz we use the place
        self.f.pack()

        self.l1 = Label(self.f, text="user name", width=10, height=2)
        self.l1.place(x=10, y=50)

        self.l3 = Label(self.f, text="password", width=10, height=2)
        self.l3.place(x=10, y=100)

        self.e1 = Entry(self.f, width=15)
        self.e1.place(y=50, x=200)

        self.e3 = Entry(self.f, width=15, show="*")
        self.e3.place(y=100, x=200)

        b1 = Button(self.f, text="LOG IN", command=self.dis, width=10, height=2)
        b1.place(x= 200, y=200)


    def dis(self):
        print(self.e1.get())
        print(self.e3.get())


a=one()
r.mainloop()


