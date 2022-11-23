try:
    cost = float(input('cost->'))
    Kyivstar = 1.4
    Life = 2.5
    Vodafone = 4.7
    print('|>-----------MENU------------<|')
    print('|         select an           |')
    print('|          operator           |')
    print('|  Kyivstar - 1.4 per minute  |')
    print('|    Life = 2.5 per minute    |')
    print('|  Vodafone = 4.7 per minute  |')
    print('|>---------------------------<|')
    action = input('action->')
    if action == 'Kyivstar':
        print(f'{1.4 * cost}UAH for {cost} minute')
    elif action == 'Life':
        print(f'{2.5 * cost}UAH for {cost} minute')
    elif action == 'Vodafone':
        print(f'{4.7 * cost}UAH for {cost} minute')

except Exception as vl_ex:
    print(f'Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')

