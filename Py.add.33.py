try:
    number = int(input('number->'))
    for i in range(1, number + 1):
        print(f'{number}*{i}={number * i}')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')