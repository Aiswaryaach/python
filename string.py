x=list(input("enter the string"))
i=0
for i in x:
    if(i!=" "):
        c=0
        for j in range(0,len(x)):
           if i==x[j]:
            c=c+1
            x[j]=' '
        print(i,"=",c)
