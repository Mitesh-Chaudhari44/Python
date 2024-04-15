#Reverse the number
# n=int(input("Enter a number to reverse: "))
# rev=0
# while(n!=0):
#     digit=n%10
#     rev= rev*10+digit
#     n=n//10
# print("Reverse of the number is",rev)

#factorial
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input())
# result=factorial(n)
# print(result)

#sum of digits
n=int(input())
s=0
while(n!=0):
    a=n%10
    s+=a
    n=n//10
print(s)