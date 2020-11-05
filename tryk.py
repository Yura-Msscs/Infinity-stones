from tkinter import*
import math

def b1_click():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    vidp2=eval(S)
    entry5.delete(0,END)
    entry5.insert(0,vidp2)
    
    if (a==b) or (c==a) or (c==b):
        if (a==b) and (b==c):
            vidp=str("rivnst")
            entry4.delete(0,END)
            entry4.insert(0, vidp)
        else:
            vidp=str("rivnbed")
            entry4.delete(0,END)
            entry4.insert(0, vidp)
    if a+b==c or b+c==a or a+c==b:
        vidp3=str("vyrazhd")
        entry4.delete(0,END)
        entry4.insert(0, vidp)
        

       
        
root = Tk()
root.title('trykutnyk')
root.geometry('650x200')
labl_1 = Label(root, text = 'a', font = 'Arial 18')
labl_1.place(x=20, y=10)
labl_2 = Label(root, text = 'b', font = 'Arial 18')
labl_2.place(x=260, y=10)
labl_3 = Label(root, text = 'c', font = 'Arial 18')
labl_3.place(x=390, y=10)

entry1 = Entry(root, text = 'a', width = 6, font = 'Arial 18')
entry1.place(x = 55, y = 10)

entry2 = Entry(root, text = 'b', width = 6, font = 'Arial 18')
entry2.place(x = 300, y = 10)

entry3 = Entry(root, text = 'c', width = 16, font = 'Arial 18')
entry3.place(x = 420, y = 10)

entry4 = Entry(root, text = 's3', width = 16, font = 'Arial 18')
entry4.place(x = 300, y = 100)

entry5 = Entry(root, text = 's4', width = 16, font = 'Arial 18')
entry5.place(x = 300, y = 150)

b1 = Button(root, text = 'vvv', command = b1_click)
b1.place(x = 150, y = 10)

p=entry1.get() + '+' + entry2.get() + '+' + entry3.get()
p2=p + '/' + '2'
S=math.sqrt(p2*(p2-entry1.get())*(p2-entry2.get())*(p2-entry3.get()))
vidp2=eval(S)
entry5.insert(0,END)
entry5.insert(o,vidp2)   
