import random
x = int(input('Enter the lower bound of the range: '))
y = int(input('Enter the upper bound of the range: '))
num = random.randint(x,y)
a=int(input('Enter your guese: '))
while a!= num:
    if a > num:
        print('Try Again! You guessed too high')
        a=int(input('enter a lower number: '))
    else:
        print('Try Again! You guessed too small')
        a=int(input('Enter a biger number: '))
if a == num:
    print('Congratulations!')