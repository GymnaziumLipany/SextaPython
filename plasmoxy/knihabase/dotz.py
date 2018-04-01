# tento skript vykresli body podla nejakeho vyroku s premennymi x a y

import tkinter as tk
import time
import random
c = tk.Canvas(width=400, height=400)
c.pack()
active = True
dt, ts, = 0, time.time()


# vyrok :
def A(x, y):
    return x**2 + y**2 <= 1


def dot(x, y, r=10):
    c.create_oval(x-r, y-r, x+r, y+r, fill='red')


def loop():
    x = random.random()*4 - 2
    y = random.random()*4 - 2
    if (A(x, y)):
        dot(x*100 + 200, 200 - y*100, 3)


def rootloop():
    global dt, ts
    nts = time.time()
    dt = nts - ts
    if (dt > 0.001):
        ts = nts

    loop()
    c.after(1, rootloop)  # rechain


c.after(1000, rootloop)
c.mainloop()
