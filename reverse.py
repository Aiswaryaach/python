x=int(input("enter the number"))
rev=0
while x>0:
   num=x%10
   rev=(rev*10)+num
   x=x//10
print("reverse of number",rev)            
