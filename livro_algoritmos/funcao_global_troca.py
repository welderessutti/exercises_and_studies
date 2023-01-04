def troca():
    global a, b
    x = a
    a = b
    b = x


a = int(input("Num 1: "))
b = int(input("Num 2: "))

print(a, b)
troca()
print(a, b)
