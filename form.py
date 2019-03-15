from tkinter import *
a=Tk()
Label(a,text='name').grid(row=1,column=1)
Label(a,text='password').grid(row=2,column=1)
Label(a,text='Mobile No.').grid(row=3,column=1)
Label(a,text='Age').grid(row=4,column=1)
c=Entry(a)
c.grid(row=1,column=4)
b=Entry(a,show="*")
b.grid(row=2,column=4)
d=Entry(a)
d.grid(row=3,column=4)
e=Entry(a)
e.grid(row=4,column=4)

def show():
    print("Name:",c.get())
    print("Password",b.get())
    print("Mobile No.",d.get())
    print("Age",e.get())
    
