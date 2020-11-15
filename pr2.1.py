from tkinter import *

def red_label():
    label['bg']='red'
def blue_label():
    label['bg']='blue'
def green_label():
    label['bg']='green'    

root=Tk()

frame=Frame()
frame.pack(side=LEFT)

var=IntVar()
var.set(0)
Radiobutton(frame, text='Red', command=red_label, variable=var, value=0, indicatoron=0).pack()
Radiobutton(frame, text='Blue', command=blue_label, variable=var, value=1, indicatoron=0).pack()
Radiobutton(frame, text='Green', command=green_label, variable=var, value=2, indicatoron=0).pack()
label=Label(width=20, height=10, bg='red')
label.pack()

root.mainloop()
