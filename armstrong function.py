def armstrongnum(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit*digit*digit
        temp=temp//10
    if n==sum:                                                                                                          
        print(n,"is an armstrong number")
    else:
        print(n,"is not a armstrong number")
y=int(input("enter a number:"))
armstrongnum(y)
