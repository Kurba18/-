print(f'|>---------MENU----------<|')
print(f'|    select the number    |')
print(f'|>-----------------------<|')
x = int(input('x->'))
if x < 0:
    print('Number is negative')
elif x == 0:
    print('Number is equal to zero')
elif x > 0:
    print('Number is positive')
input()

