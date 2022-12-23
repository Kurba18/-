try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    if begin > end:
        begin, end = end, begin

    while True:
        number = int(input('number->'))
        if begin <= number <= end:
            for i in range(begin, end+1):
                if i < number or i > number:
                    print(i, end=' ')
            else:
                print(f'!{number}!', end=' ')
        break
    else:
        print('Error the number is not included in the loop')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')


