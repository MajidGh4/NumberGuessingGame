import random
import math
x = int(input('Enter the lower bound of the range: '))
y = int(input('Enter the upper bound of the range: '))
num = random.randint(x,y)
Minimum_Guesses = int(math.log2(y-x+1))
Guess_Counter = 0
a=int(input('Enter your guese: '))
Guess_Counter =+ 1
while a!= num:
    if a > num:
        print('Try Again! You guessed too high')
        a=int(input('Enter a lower number: '))
        Guess_Counter += 1
        if (Guess_Counter == Minimum_Guesses):
            print('Better Luck Next Time')
            break
    else:
        print('Try Again! You guessed too small')
        a=int(input('Enter a biger number: '))
        Guess_Counter += 1
        if (Guess_Counter == Minimum_Guesses):
            print('Better Luck Next Time')
            break
if a == num:
    print('Congratulations!')