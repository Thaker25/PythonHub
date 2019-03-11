import re
Total_balance=200
password=input("Enter password")

if password=="DaveDT":
    
    print("f:Frankie,ch=Chocolate,w=Waffles,fr=Fries,m=Milkshakes")
    item=input("Enter food item:")

    if item=='f':
        balance=Total_balance-60
        print("Frankie")
        
    if item=='ch':
        balance=Total_balance-40
        print("Chocolate")

    if item=='w':
        balance=Total_balance-50
        print("Waffles")

    if item=='fr':
        balance=Total_balance-30
        print("Fries")

    if item=='m':
        balance=Total_balance-55
        print("Milkshakes")

elif password!=DaveDT:

    print("Password invalid")
    

if password=="DaveDT":
    print("Remaining Balance",balance)
