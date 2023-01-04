def x(n):
    if n == 0:
        print(n)
    else:
        x(n - 1)
        print(n)


x(10)


def y(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return y(n-1) + y(n-2) + y(n-3)


print(y(6))
