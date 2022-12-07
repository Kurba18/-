try:
    number = float(input('number->'))
    while number <= 100000:
        number = number - 1
        print(number)
        if 0 >= number:
           raise Exception('high can not be <= 0')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')





