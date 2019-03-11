#a_key = ['a','b','c','d','e','f']
#b_value = [1,3,5,7,9,11]

#print(list(zip(a_key,b_value)))


a = input("Enter name")
d= {"Letter":0 , "digits":0}
c=0
b=0
for i in a:
    if i.isalpha():
        c=c+1
    else:
        i.isdigit()
        b=b+1

d["Letter"]=c
d["digits"]=b

print(d)
        
    

