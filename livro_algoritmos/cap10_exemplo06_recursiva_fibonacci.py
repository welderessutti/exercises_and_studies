def fibonacci(n):
    while not n <= 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return 1


for a in range(0, 100):
    print(fibonacci(a))
