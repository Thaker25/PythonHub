from socket import *

a=socket()
a.connect(("localhost",1111))
a.send("Hello".encode("ascii"))
a.close()
