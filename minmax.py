l = [1,2,3,4,8,10,16,15]


  
def ad(a):
    print(a)
    max1=a[0]
    
    for item in a:
        if max1 < item:
            max1=item
    print(max1)
    


ad(l)
