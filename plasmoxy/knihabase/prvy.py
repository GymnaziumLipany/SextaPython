import tkinter
c = tkinter.Canvas(bg='black', width=500, height=500)
c.pack()


def axis(x, y, inv):
    for i in range(0, 25):
        x += 20 if not inv else -20
        y += 20 if not inv else -20
        c.create_line(x, 10, 510, y, fill='orange', width=2)
        c.update()
        c.after(100)


axis(0, 0, False)
axis(0, 500, True)

c.after(2000)
