from tkinter import *
root = Tk()
root.title("TEMPERATURE CONVERSION")

class convert:
    def __init__(self):

        self.ft = 0.0
        self.ct = 0.0

        self.f = Frame(width=800, height=1200)
        self.f.pack()

        self.l = Label(self.f, text="The computed temperature value will be...", fg="black")
        self.l.place(x= 220, y= 180)

        self.l1 = Label(self.f, text="Enter temperature :",height=2, width=20)
        self.l1.place(x=50, y=50)

        self.e1 = Entry(self.f, width=15)
        self.e1.place(x=220, y=55)

        self.x = IntVar()

        self.rb1 = Radiobutton(self.f, text="CELSIUS", variable=self.x, value=1)
        self.rb2 = Radiobutton(self.f, text="FAHRENHEIT", variable=self.x, value=2)

        self.rb1.place(x= 220, y= 100)
        self.rb2.place(x= 350, y= 100)

        b1 = Button(self.f, text="CONVERT", command=self.con, width=10, height=2)
        b1.place(x= 220, y=140)


    def con(self):

        if self.x.get() == 1:
            self.ct = float(self.e1.get())
            self.ft = ((self.ct * (9/5)) + 32)
            self.l.config(text="TEMP IN FAHRENHEIT IS "+str(self.ft))
        else:
            self.ft = float(self.e1.get())
            self.ct = ((self.ft - 32) * (5/9))
            self.l.config(text="TEMP IN CELSIUS IS "+str(self.ct))

c = convert()
root.mainloop()


