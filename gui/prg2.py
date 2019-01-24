from tkinter import *
root = Tk()
root.geometry("1200x800+100+100")
root.title("house")
c = Canvas(root, height=800, width=1200, bg="sky blue")

c.create_oval(100,100,200,200,fill="yellow",outline="sky blue",activefill="sky blue")

c.create_rectangle(800,200,450,600,fill="blue",outline="green")

c.create_polygon(800,200,450,200,630,50,fill="green")

c.create_rectangle(600,600,450,450,fill="brown")









c.pack()
root.mainloop()

