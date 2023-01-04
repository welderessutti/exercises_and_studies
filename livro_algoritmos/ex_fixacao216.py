x = 1
a = 3
b = 5
c = 8
d = 7

if not x > 3:
    print('a) verdadeiro')
else:
    print('a) falso')

if x < 1 and not b > d:
    print('b) verdadeiro')
else:
    print('b) falso')

if not d < 0 and c > 5:
    print('c) verdadeiro')
else:
    print('c) falso')

if not x > 3 or c < 7:
    print('d) verdadeiro')
else:
    print('d) falso')

if a > b or c > b:
    print('e) verdadeiro')
else:
    print('e) falso')

if x >= 2:
    print('f) verdadeiro')
else:
    print('f) falso')

if x < 1 and b >= d:
    print('g) verdadeiro')
else:
    print('g) falso')

if d < 0 or c > 5:
    print('h) verdadeiro')
else:
    print('h) falso')

if not d > 3 or not b < 7:
    print('i) verdadeiro')
else:
    print('i) falso')

if a > b or not c > b:
    print('j) verdadeiro')
else:
    print('j) falso')

