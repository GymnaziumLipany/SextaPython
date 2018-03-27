from tkinter import *

active = True
x, y = 0, 0

canvas = Canvas()
canvas.pack()

def motion(event):
    global x,y
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))

canvas.bind('<B1-Motion>', motion);

while active:
    canvas.create_oval(x-10, y-10, x+10, y+10)
    canvas.update_idletasks()
    canvas.update()
