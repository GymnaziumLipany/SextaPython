import tkinter as tk
c = tk.Canvas(width=400, height=400)
c.pack()


def dot(x, y, r=10):
    c.create_oval(x-r, y-r, x+r, y+r, fill='red')
    c.after(1000)


dot(100, 100)
dot(200, 200)

c.after(2000)
