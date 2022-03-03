
f=open("file1.txt","r")
s=f.read()
f.close()

f=open("file2.txt","w")
f.write(s)
f.close()
