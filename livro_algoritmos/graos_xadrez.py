q1 = 1
soma1 = 1
cont = 1

print(1, end=' ')
print(1)

while cont <= 64:
    q2 = q1 * 2
    soma2 = soma1 + q2
    q1 = q2
    soma1 = soma2
    print(q2, end=' ')
    print(soma2)
    cont += 1
