def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def coefbinomi(n, k):
    res = fatorial(n) // (fatorial(k) * fatorial(n - k))
    return res


print(fatorial(5))
print(coefbinomi(20, 10))
