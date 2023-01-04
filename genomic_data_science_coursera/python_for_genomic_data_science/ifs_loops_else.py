n = 10

for y in range(2, n):
    for x in range(2, y):
        if y % x == 0:
            print(f"{y} equals {x} * {y // x}")
            break
    else:
        print(f"{y} is a prime number.")

seq = "welderressutti"


for i in range(len(seq) + 1):
    for j in range(i):
        print(seq[j:i])

l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0]
l2 = [1, 6, 3, 9, 5, 1, 2, 3, 4, 5, 0, 0, 0]
l3 = []

for elem in l1:
    if elem in l2 and elem not in l3:
        l3.append(elem)

print(l3)

mylist = [1, 2, 2, 3, 4, 5]

d = {}
result = False
for x in mylist:
    if x not in d:
        d[x] = True
        continue
    result = True

print(result)
print(d)

x = 0
if x > 10 or x < -10:
    print('big')
elif x > 1000000:
    print('very big')
elif x < -1000000:
    print('very big')
else:
    print('small')

i = 1
while i < 100:
    if i % 2 == 0:
        break
    i += 1
else:
    i = 1000

print(i)
