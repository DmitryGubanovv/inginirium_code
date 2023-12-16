import tkinter as tk

a = tk.Tk()
c = tk.Canvas(a, bg="#fff", width=400, height=400)
for i in range(0, 400, 50):
    c.create_line((i, 0), (i, 400), fill="#000")
    c.create_line((0, i), (400, i), fill="#000")
for i in range(8):
    for j in range(3):
        if (i+j)%2 == 0:
            c.create_oval((i*50,j*50), (i*50+50,j*50+50),fill="#0f0")
    for j in range(5,8):
        if (i+j)%2 == 0:
            c.create_oval((i*50,j*50), (i*50+50,j*50+50),fill="#0ff")

c.pack()
a.mainloop()
