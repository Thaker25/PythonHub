class rect:
    def __init__(self):
        self.a=int(input("enter the length of rectangle:"))
        self.b=int(input("enter the breadth of rectangle:"))
        
    def area(self):
        self.c= self.a * self.b        
        print(self.c)
    def par(self):
        self.e=2*(self.a*self.b)
        print(self.e)
        

obj=rect()
obj.area()
obj.par()

        
     
