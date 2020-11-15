from tkinter import *

def red_label():
    label['text']='Галушки'
    label['bg']='white'
def blue_label():
    label['text']='Борщ'
    label['bg']='white'
def green_label():
    label['text']='Вареники'
    label['bg']='white'

root=Tk()
root.title('Страви учасниць конкурсу')

frame=Frame()
frame.pack(side=LEFT)

var=IntVar()
var.set(0)
Radiobutton(frame, text='Таня', command=red_label, variable=var, value=0, indicatoron=0).pack()
Radiobutton(frame, text='Маша', command=blue_label, variable=var, value=1, indicatoron=0).pack()
Radiobutton(frame, text='Катя', command=green_label, variable=var, value=2, indicatoron=0).pack()
label=Label(width=20, height=10, text='Галушки', bg='white')
label.pack()

root.mainloop()
