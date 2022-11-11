x = float(input("x->"))
print('1. convert to miles \n 2. convert to inches \n 3. convert to yards')
action = int(input('enter number'))
if action == 1:
   print(x * 0.000621371192)
elif action == 2:
   print(x * 39.3700787)
elif action == 3:
   print(x * 1.0936133)
   input()