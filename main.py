from tkinter import *


def hello(event):
    print("Single Click, Button-1")


def quit1(event):
    print("Double Click so lets stop")
    import sys
    sys.exit()


b1 = Button(None, text=" Mouse Click")
b1.bind('<Button-1>', hello)
b1.pack()
b1.bind('<Double-1>', quit1)
b1.mainloop()
