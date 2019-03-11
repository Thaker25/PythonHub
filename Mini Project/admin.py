from pymysql import *
a=connect("localhost","root","tiger","Vendingmc")
a.cursor()
b=a.cursor()
x=input("Product Name")
y=input("Price of Product")
c="insert into admin(product,price)values('{}','{}')".format(x,y)
b.execute(c)
a.commit()

