import tkinter as tk

def pnt(evt):
    cvs.create_oval(x - sz, y - sz, x + sz, y + sz, outline=clr, fill=clr)

def sizeble(evt):
    global sz, oval
    if evt.keysym == 'Up' and sz <100:
        sz += 1
    if evt.keysym == 'Down' and sz > 0:
        sz -= 1
    lb.config(text=f"sz of brush {sz} px")
    cvs.delete(oval)
    oval = cvs.create_oval(x-sz, y-sz, x+sz, y+sz, fill=clr)

def ms_ps(evt):
    global x, y
    x = evt.x
    y = evt.y

    cvs.moveto(oval, x-sz, y-sz)

r = tk.Tk()
r.t = ('Brush')
sz = 5
x, y = 0, 0
clr = '#0f0'
lb = tk.Label(r,text=f"sz of brush {sz} px")
lb.pack()
cvs = tk.Canvas(r, bg="#fff", width=640, height=640)
oval = cvs.create_oval(x-sz, y-sz, x+sz, y+sz, fill=clr)
cvs.pack()
r.bind('<KeyPress>', sizeble)
r.bind('<Motion>', ms_ps)
r.bind('<Button-1>',pnt)

r.mainloop()