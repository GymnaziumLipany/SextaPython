import tkinter
c = tkinter.Canvas(bg='black', width=1000, height=800)
c.pack()


def axis(x, y):
    for i in range(0, 25):
        x += 20
        y += 20
        c.create_line(x, 10, 510, y, fill='white', width=2)
        c.update()
        c.after(100)


c.mainloop()
