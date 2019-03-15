class marksheet:
   
    def __init__(self):
        self.name = input("Enter name:")
        self.age = int(input("Enter Age:"))
        self.gender = input("Enter gender:")

    def display(self):
        print("\n\nName:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

class Marks:

    def __init__(self):
        self.Science = int(input("Enter marks of Science:"))
        self.Maths = int(input("Enter marks of Maths:"))
        self.Sanskrit = int(input("Enter marks of Sanskrit:"))

    def display(self):
        Total = self.Science + self.Maths + self.Sanskrit
        print("Total Marks:",Total)

                       
class student(marksheet,Marks):
    
    def __init__(self):
        marksheet. __init__self()
        marks. __init__self()
        

m1=marksheet()
m2=Marks()
m1.display()
m2.display()

                   
                   
                   
                       
                   
                       
            
               
                       
                    


                  
                  
        
    
    
