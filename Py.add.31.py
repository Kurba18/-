try:
    number = int(input('number->'))
    if number > 0:
        print('Number is positive')
    elif number < 0:
        print('Number is negative')
    elif number == 0:
        print('Number is equal zero')
    if number == 7:
        print('Good bye!')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')

