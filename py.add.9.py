try:
    number = int(input('number->'))
    if number % 7 == 0:
        print('Number is multiple 7')
    elif number % 7 != 0:
        print('Number is not multiple 7')
    else:
        print(number)
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')