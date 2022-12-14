try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    for i in range(begin, end + 1):
        print(i, end=" ")
        if i % 3 == 0:
            print('fizz', end=" ")
        if i % 5 == 0:
            print('buzz', end=" ")
        print()
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')