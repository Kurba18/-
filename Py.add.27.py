begin = int(input('begin->'))
end = int(input('end->'))
for i in range(begin, end + 1):
    print('\n', i)
for i in range(end, begin, -1):
    print('\n', i)
for i in range(begin, end + 1):
    if i % 7 == 0:
        print('\n', i)
for i in range(begin, end + 1):
    if i % 5 == 0:
        print('\n', i)













