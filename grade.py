a=int(input("enter the first subject mark"))
b=int(input("enter the second subject mark"))
c=int(input("enter the third subject mark"))
d=int(input("enter the fourth subject mark"))
e=int(input("enter the fifth subject mark"))
total=a+b+c+d+e
print("Total is",total)
average=total/5
print("average of mark is",average)
if average>80:
    print("good")
elif average<50:
    print("average")
elif  average>40:
    print("passed")
else:
    print("fail")
    
