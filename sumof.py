x=int(input("Enter the value"))
s=a=0
while x>0:
    a=x%10
    s=s+a
    x=x//10
print("sum of digit is",s)
