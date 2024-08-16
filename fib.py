def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sum = 1
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fib_sum += b
        return fib_sum

# Fibonacci series: 0, 1, 1, 2, 3, 5
series_length = 6
print("Sum of Fibonacci series is:", fibonacci_sum(series_length))
