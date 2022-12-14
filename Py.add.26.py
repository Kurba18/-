try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    for i in range(begin, end + 1):
        if i % 7 == 0:
            print(i, end='\t')
except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')