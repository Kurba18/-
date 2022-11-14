gigabyte = float(input('gigabyte->'))
speed_bit = float(input('speed_bit->'))
print('#>---<MENU>----<#')
print('|  h - hour     |')
print('|  m - minutes  |')
print('|  s - seconds  |')
print('#>------------------------<#')
action = (input('action->'))
if action == 's':
    print(f'seconds: {gigabyte / speed_bit}')
elif action == 'm':
    print(f'minutes: {gigabyte / speed_bit / 60}')
elif action == 'h':
    print(f'hour: {gigabyte / speed_bit / 60 / 60}')
input()


