try:
    number = int(input('number->'))
    if 0 >= number:
        raise Exceptation('Number is can not ba <= 0')
    print('|>------MENU------<|')
    print('|  Enter degree1   |')
    print('|  Enter degree2   |')
    print('|  Enter degree3   |')
    print('|  Enter degree4   |')
    print('|  Enter degree5   |')
    print('|  Enter degree6   |')
    print('|  Enter degree7   |')
    print('|>----------------<|')
    action = input('action->')
    if action == 'degree1':
       degree1 = number
       print(degree1)
    elif action == 'degree2':
       degree2 = number*number
       print(degree2)
    elif action == 'degree3':
       degree3 = number*number*number
       print(degree3)
    elif action == 'degree4':
       degree4 = number*number*number*number
       print(degree4)
    elif action == 'degree5':
       degree5 = number*number*number*number*number
       print(degree5)
    elif action == 'degree6':
       degree6 = number*number*number*number*number*number
       print(degree6)
    elif action == 'degree7':
       degree7 = number*number*number*number*number*number*number
       print(degree7)
    else:
        print(f'command not found')

except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')



