def oddeven1(x):
     s=x%2
     return(s)
y=int(input("enter  number:"))
odev=oddeven1(y)
if(odev==0):
     print("even")
else:
    print("odd")
