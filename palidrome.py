x=int(input("enter anumber"))
temp=x
rev=0
while x>0:
    num=x%10
    rev=(rev*10)+num
    x=x//10
if temp==rev:
    print("num is palidrome")
else:
    print("num is not palidrome")
