x=int(input("enter the number"))
i=1
c=0
while i<=x:
    if x%i==0:
        c=c+1
    i=i+1
if c==2:
    print("number is prime number")
else:
    print("number is not prime number")
