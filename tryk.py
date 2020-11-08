from tkinter import*
import math

#Function
def b1_click():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
        
    if (a==b) or (a==c) or (b==c):
        if (a==b) and (b==c):
            vidp=str("рівносторонній")
            entry4.delete(0, END)
            entry4.insert(0, vidp)
        else:
            vidp=str("рівнобедрений")
            entry4.delete(0, END)
            entry4.insert(0, vidp)
        
    if (a+b<=c) or (b+c<=a) or (a+c<=b):
        vidp=str("неправильний")
        entry4.delete(0, END)
        entry4.insert(0, vidp)

    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2):
        vidp=str("прямокутний")
        entry4.delete(0, END)
        entry4.insert(0, vidp)
        
    if (a+b<c) or (b+c<a) or (a+c<b):
        vidp=str("S не можливе")
        entry5.delete(0, END)
        entry5.insert(0, vidp)
    else:
        s=math.sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))
        vidp=float(s)
        entry5.delete(0, END)
        entry5.insert(0, vidp)

#Window        
root = Tk()
root.title('трикутник')
root.geometry('450x200')

#Labels
labl_1 = Label(root, text = 'a', font = 'Arial 18')
labl_1.place(x=20, y=10)

labl_2 = Label(root, text = 'b', font = 'Arial 18')
labl_2.place(x=160, y=10)

labl_3 = Label(root, text = 'c', font = 'Arial 18')
labl_3.place(x=300, y=10)

labl_4 = Label(root, text = 'Tип трикутника', font = 'Arial 18')
labl_4.place(x=160, y=50)

labl_5 = Label(root, text = 'Площа трикутника', font = 'Arial 18')
labl_5.place(x=160, y=125)

#Entries
entry1 = Entry(root, text = 'a', width = 6, font = 'Arial 18')
entry1.place(x = 55, y = 10)

entry2 = Entry(root, text = 'b', width = 6, font = 'Arial 18')
entry2.place(x = 200, y = 10)

entry3 = Entry(root, text = 'c', width = 6, font = 'Arial 18')
entry3.place(x = 345, y = 10)

entry4 = Entry(root, text = 's3', width = 15, font = 'Arial 18')
entry4.place(x = 160, y = 90)

entry5 = Entry(root, text = 's4', width = 15, font = 'Arial 18')
entry5.place(x = 160, y = 160)

#Button
b1 = Button(root, text = 'vvv', command = b1_click, width = 8, height = 4, font = 'Arial 18')
b1.place(x = 20, y = 60)

  
