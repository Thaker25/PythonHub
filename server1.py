from socket import *
a=socket()
a.bind(("localhost",1111))
a.listen(5)
while True:
    c,d= a.accept()
    e=c.receive(1024)
    print(e.decode())
    c.close()
       
       
    
