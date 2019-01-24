'''
the below code is for entry and taking input from the text box
'''
from tkinter import *
r=Tk()
r.geometry("1200x800+100+100")


class one:
    def __init__(self):
        self.f = Frame(width=800, bg="blue", height=1200)    # height and width is not default coz we use the place
        self.f.pack()

        self.l1 = Label(self.f, text="name", width=10, height=2)
        self.l1.place(x=10, y=50)

        self.l2 = Label(self.f, text="roll", width=10, height=2)
        self.l2.place(x=10, y=100)

        self.l3 = Label(self.f, text="marks", width=10, height=2)
        self.l3.place(x=10, y=150)

        self.e1 = Entry(self.f, width=15)
        self.e1.place(y=50, x=200)

        self.e2 = Entry(self.f, width=15)
        self.e2.place(y=100, x=200)

        self.e3 = Entry(self.f, width=15, show="*")
        self.e3.place(y=150, x=200)

        self.e3.bind('<Return>', self.dis)

    def dis(self, event):    # event is passed coz no submit button needs enter as an event to perform action and bind is not needed

        print(self.e1.get())
        print(self.e2.get())
        print(self.e3.get())

a=one()
r.mainloop()


