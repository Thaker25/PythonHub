class A:
    def __init__(self):
        self.a=10

class B:
    def add(self):
        self.b=20
        self.c=self.a+self.b
        print(self.c)
