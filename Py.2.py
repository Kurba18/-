a = int(input())
b = int(input())
for i in range(1, 10):
    print(a, 'x', i, '=', a * i, end='   |   ')
    print(b, 'x', i, '=', b * i)