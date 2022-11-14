user_d = float(input('diameter->'))
radius = user_d / 2
circumference = float(2 * 3.14 * radius)
area = float(3.14 * radius * radius)
print('#>---------<MENU>---------<#')
print('|    c - circumference     |')
print('|        of circle         |')
print('|       a - area of        |')
print('|         circle           |')
print('#>------------------------<#')
action = (input('action->'))
if action == 'c':
    print(circumference)
elif action == 'a':
    print(area)
input()



