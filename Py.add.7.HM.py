print(f'|>----------MENU----------<|')
print(f'|    select the numbers    |')
print(f'|>------------------------<|')
x = int(input('x->'))
y = int(input('y->'))
if x < y:
    print(f'{x};{y}')
if y < x:
    print(f'{y};{x}')
if y == x:
    print(f'{y}={x}')