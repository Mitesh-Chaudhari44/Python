def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter n: "))
result = factorial(n)
print("Factorial of", n, "is", result)