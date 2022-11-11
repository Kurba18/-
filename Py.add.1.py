x = float(input('number one->'))
y = float(input('number two->'))
z = float(input('number three->'))
print('|>-------------MENU---------------<|')
print(f'| + : enter sum for {x} + {y} + {z}|')
print(f'| - : enter dif for {x} - {y} - {z}|')
print(f'|>--------------------------------<|')
action = input('action->')
if action =='+':
    print(f'{x} + {y} + {z} = {x+y+z}')
elif action == '-':
    print(f'{x} - {y} - {z} = {x-y-z}')
    input()
