n=int(input("Enter n "))
count=0
temp = n
while(n>0):
    n = n//10
    count=count+1
if(count==1):
    print(temp**2)
elif(count==2):
    print(temp**0.5)
elif(count==3):
    print(temp**(1/3))
else:
    print("N is grater than 3 digit")