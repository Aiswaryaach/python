s=lambda a:a*a
r=lambda c,d:c*d
t=lambda l,b,h:l*b*h/2
x=int(input("enter the side of square:"))
print("area of square",s(x))

y=int(input("enter the length of rectangle:"))
z=int(input("enter the breadth of rectangle:"))
print("area of rectangle",r(y,z))

s=int(input("enter the length of triangle:"))
v=int(input("enter the breadth of triangle:"))
w=int(input("enter the heigth of triangle:"))

print("area of triangle",t(s,v,w))
