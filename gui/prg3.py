# button and its Button ie case sensitive

from tkinter import *
r = Tk()

f = Frame(r, height=200, width=500, bg="black")  # frame is created and needs to be packed

f.propagate(0) # for window to be of correct width and height

fnt = ("fore",18,"bold")

b = Button(f, text="CLICk", font=fnt, height=2, width=10, bg="blue", fg="red", activebackground="red", activeforeground="blue")  # bg is bg color and fg is text color

b.pack() # very imp part each button needs to be pacled

b1 = Button(f, text="button 2", command=lambda: handle_c(10))
b1.pack()
b2 = Button(f, text="button 3", command=lambda: handle_c(20))
b2.pack()
b3 = Button(f, text="destroy", command= r.destroy, width=10, height=2, font=fnt)  #command= f.destroy or f.pack_forget or r.destroy to close window
b3.pack()

def handle_c(cb):
    if cb==10:
        print("no 1")
    else:
        print("no 2")


def handler_b(self):
    print("clicked")


b.bind('<Button-1>', handler_b)  # <Button-1> is case sensitive   # default is left clicked
# whenever button 'b' is clicked with button-1(left click) and when clicked handler_b() is called

f.pack()
r.mainloop()


"""
b = Button(f, text="CLICk", bg="blue", fg="red", command = handler_b)
now b,bind id not needed coz of command 
def has to be defined before 

now def has to be defined without (self) parameter coz as u can see command does not send any param
"""