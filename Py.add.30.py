try:
    begin = 1
    number = int(input('number->'))
    for i in range(begin, number + 1):
        print('*')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')

