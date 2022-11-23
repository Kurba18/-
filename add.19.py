try:
    print(f'|>------------MENU-------------<|')
    print(f'| choose the total of the sale  |')
    print(f'|     high - 1000-100000 8%     |')
    print(f'|      middle - 500-1000 5%     |')
    print(f'|         low - 0-500 3%        |')
    print(f'|>-----------------------------<|')
    salary = 200
    high = 1000
    while high <= 100000:
        high = high + 1
    high = float(input('high->'))
    if 0 >= high:
        raise Exception('high can not be <= 0')
    if 1000 >= high:
        raise Exception('high can not be <= 1000')
    middle = 1000
    while middle >= 500:
        middle = middle - 1
    middle = float(input('middle->'))
    if 0 >= middle:
        raise Exception('middle can not be <= 0')
    if 1000 <= middle:
        raise Exception('middle can not be >= 1000')
    if 500 >= middle:
        raise Exception('middle can not be <= 500')
    low = 500
    while low >= 1:
        low = low - 1
    low = float(input('low->'))
    if 0 >= low:
        raise Exception('low can not be <= 0')
    if 500 <= low:
        raise Exception('low can not be >= 500')
    print(f'|>------------MENU-------------<|')
    print(f'|    select the manager level   |')
    print(f'|             high              |')
    print(f'|            middle             |')
    print(f'|              low              |')
    print(f'|>-----------------------------<|')
    manager1 = (input('manager1->'))
    if manager1 == 'low':
        print(f'{low * 3 / 100 + salary}')
    elif manager1 == 'middle':
        print(f'{middle * 5 / 100 + salary}')
    elif manager1 == 'high':
        print(f'{high * 8 / 100 + salary}')
    manager2 = (input('manager2->'))
    if manager2 == 'low':
        print(f'{low * 3 / 100 + salary}')
    elif manager2 == 'middle':
        print(f'{middle * 5 / 100 + salary}')
    elif manager2 == 'high':
        print(f'{high * 8 / 100 + salary}')
    manager3 = (input('manager3->'))
    if manager3 == 'low':
        print(f'{low * 3 / 100 + salary}')
    elif manager3 == 'middle':
        print(f'{middle * 5 / 100 + salary}')
    elif manager3 == 'high':
        print(f'{high * 8 / 100 + salary}')

except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')


