from tkinter import *

window = Tk()

c=Canvas(window)
c.create_oval(45,40,125,120,fill='lightblue')
c.create_oval(55,55,85,85,fill='white')
c.create_oval(85,55,115,85,fill='white')
c.create_oval(60,60,80,80,fill='black')
c.create_oval(90,60,110,80,fill='black')
c.create_oval(82,85,88,91,fill='red')
c.create_arc(70,100,100,90,start=0,extent=-180,style=ARC)
c.pack()
mainloop()
