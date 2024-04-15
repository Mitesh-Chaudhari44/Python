f =open('file.txt','r')
x=f.read()
l = list(x.split())
print("Word count is : ",len(l))

