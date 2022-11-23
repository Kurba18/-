try:
    number = int(input('number->'))
    if number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('fizz')
    elif number % 3 != 0 and number % 5 != 0:
        print('fizz buzz')
    else:
        print(number)

except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')