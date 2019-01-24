from tkinter import *
root = Tk()
root.geometry("400x500+100+100")   # 400 width 500 height horizontal and vertical displacement(top left corner dist)
root.title("hello")
c = Canvas(root, height=500, width=400, bg="yellow")

c.create_line(100,100,200,100,200,200,fill="red",activefill="blue",width=5)   # first 4 parameter are points 3rd parameter is next point the line

c.create_rectangle(200,200,100,300,fill="blue",width=5,outline="white")     # diagonally opposite points here fill will fill color inside shape

c.create_polygon(200,200,300,200,200,100,smooth=True) # smooth tangesnts each point in polygon and creates oval
# it specifies the vertices in parameters and triangle can also be made fill is default black

c.create_oval(100,100,200,200,width=5,fill="grey")  # oval(x postion y postion from top and left x axis of circle and then y axis

f1 = ("forte", 20, "bold italic underline")

c.create_text(100,350,text="hi hello",font=f1,anchor=SW)   # 100 is from left and 350 is from top

c.create_arc(200,180,80,50,start=210,extent=120,width=5,style="arc") # after start moves in anti clock wise direction

i1 = PhotoImage(file="1.png")

c.create_image(0,600,image=i1,anchor=SW)



c.pack()
root.mainloop()                    # this let the window stay for the user to interact




