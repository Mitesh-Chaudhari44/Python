n=int(input("Enter n"))
def rec_fib(n):
    if(n==0 or n==1):
        return n
    else:
        return(rec_fib(n-1)+rec_fib(n-2))
for i in range(0,n):
        print(rec_fib(i))
        