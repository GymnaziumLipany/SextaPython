import tkinter as tk
root = tk.Tk()
c = tk.Canvas(width=800, height=600)
c.pack()


def stredObdl(x, y, d):
    c.create_rectangle(x-d, y-d, x+d, y+d, outline='red')


for i in range(20, 300, 10):
    stredObdl(400, 300, i)

c.mainloop()
