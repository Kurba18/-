x = float(input('number one->'))
y = float(input('number two->'))
print('f|>------------MENU-------------<|')
print(f'|  press {1} for higher number  |')
print(f'|  press {2} for lower number   |')
print(f'|  press {3} for arithmetic mean|')
print(f'|>-----------------------------<|')
action = int(input('action->'))
if action == 1:
  print (x+y)
elif action == 2:
  print (x-y)
elif action == 3:
  print (f'armean = {(x+y)/2}')