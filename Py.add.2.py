x = float(input('number one->'))
y = float(input('number two->'))
z = float(input('number three->'))
print('|>------------MENU-----------<|')
print(f'|  press {1} for higher number  |')
print(f'|  press {2} for lower number   |')
print(f'|  press {3} for arithmetic mean|')
action = int(input('action'))
armean = int(input('action'))
if action == 1:
  print (max(x, y, z))
elif action == 2:
  print (min(x, y, z))
elif armean == 3:
  print (f'armean = {(x+y+z)/3}')
  input()