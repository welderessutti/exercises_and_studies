x = 1
y = 2

x, y = y, x

print(x, y)


def f1(x):
    if x > 0:
        x = 3*x
        x = x / 2
    return x


def f2(x):
    if x > 0:
        x = 3 * x
    x = x / 2
    return x


print(f1(2))
print(f2(2))


def function1(length):
    if length > 0:
        print(length)
        function1(length - 1)


'''def function2(length):
    while length > 0:
        print(length)
        function2(length - 1)'''


print(function1(3))
'''print(function2(3))'''


def compute(n, x, y):
    if n == 0: return x
    return compute(n-1, x + y, y)


print(compute(10, 2, 10))


def valid_dna1(dna):
    for c in dna:
        if c in 'acgtACGT':
            return True
        else:
            return False


def valid_dna2(dna):
    for c in dna:
        if 'c' in 'acgtACGT':
            return 'True'
        else:
            return 'False'


def valid_dna3(dna):
    for c in dna:
        flag = c in 'acgtACGT'
    return flag


def valid_dna4(dna):
    for c in dna:
        if not c in 'acgtACGT':
            return False
    return True


dna_valid = valid_dna4("tcagctagctagctagctagctagctgwatcgatcggatgctagcww")
print(dna_valid)


L1 = [1, 1, 2, 2, 3]
L2 = [1, 1, 2, 2, 4]

L3 = [i for i in set(L1) if i in L2]

print(L3)
print(type(L3))


def f(mystring):
         print(message)
         print(mystring)
         message="Inside function now!"
         print(message)
message="Outside function!"
f("Test function:")
