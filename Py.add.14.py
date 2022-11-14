print('#>-----------<MENU>-----------<#')
print('|        coast of console      |')
print('|          * 10 000 *          |')
print('|      amount and percent      |')
print('#>----------------------------<#')
console = True
while console:
    if (input('Price is : ')) == '10000':
        console = False
        amount = int(input('amount->'))
i = 0
while i == 0:
    price = (10000 * amount)
    percent = int(input('percent->'))
    x = price / 100 * percent
    print(price - x)
input()


