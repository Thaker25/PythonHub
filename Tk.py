from tkinter import *
from pqmysql import *
a=pymysql.connect("localhost","root","tiger","test")
a= Tk()
def show():
    print("Hello")
    print(a1.get())
    print(a2.get())
    print(a3.get())
    print(a4.get())
    
Label(a,text="First Name").grid(row=2,column=12)
a1=Entry(a)
a1.grid(row=2,column=13)
Label(a,text="Last Name").grid(row=3,column=12)
a2=Entry(a)
a2.grid(row=3,column=13)
Label(a,text="Mobile No.").grid(row=4,column=12)
a3=Entry(a)
a3.grid(row=4,column=13)
Label(a,text="Email ID").grid(row=5,column=12)
a4=Entry(a)
a4.grid(row=5,column=13)
Button(a,text="Submit",command=show).grid(row=6,column=12)
    
    




