# button and its Button ie case sensitive

from tkinter import *
r = Tk()
r.geometry("200x500+100+100")

f = Frame(r, height=500, width=200)

f.propagate(0)

fnt = ("fore",18,"bold")


b1 = Button(f, text="RED", command=lambda: handle_c(10), width=10, height=2, font=fnt)
b1.pack()           # more parameters in note book
b2 = Button(f, text="BLUE", command=lambda: handle_c(20), width=10, height=2, font=fnt)
b2.pack()
b3 = Button(f, text="EXIT", command=f.pack_forget, width=10, height=2, font=fnt)
b3.pack()

def handle_c(cb):
    if cb == 10:
        f["bg"]="red"
    else:
        f["bg"]="blue"

f.pack()

b4 = Button(r, text="appear", command=f.pack)   # interesting to call back the frame
b4.pack()


#f.pack()
r.mainloop()


