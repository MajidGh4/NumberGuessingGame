import random
num = random.randint(1,100)
a=int(input('enter your guese: '))
while a!= num:
    if a > num:
        print('biger')
        a=int(input('enter a lower number: '))
    else:
        print('lower')
        a=int(input('enter a biger number: '))
if a == num:
    print('correct')