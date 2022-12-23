from random import randint
from datetime import *
fixTime1 = datetime.now()
for i in range(1):
    a = randint(1,500)
    print('a hint for user :',a)

    while True:
        number = int(input('number->'))
        if a < number:
            print('wrong, try a lower number')
        elif a > number:
            print('wrong, try a higher number')
        else:
            print(f'correct, you guessed the number in {i} tries')
            break
        fixTime2 = datetime.now()
        print()
        print(f'Start time: {fixTime1.strftime("%H:%M:%S")}')
        print(f'End time: {fixTime2.strftime("%H:%M:%S")}')
        print(f'between: {fixTime2 - fixTime1} ')





