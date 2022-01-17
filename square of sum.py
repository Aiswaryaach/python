def square(x):
    sq=x*x
    s=0
    print("square of number:",sq)
    while sq>0:
        s=s+sq%10
        sq=sq//10
    print("sum of",s)
    if s==x:
        print("this number is neon")
    else:
        print("this number is not neon")

y=int(input("enter a value:"))
square(y)
