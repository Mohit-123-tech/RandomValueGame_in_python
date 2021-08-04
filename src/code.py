import os
import random

numbers = '1234567890'
all = numbers
lenght = 2
randomValue = ''.join(random.sample(all, lenght))

print('\n ========={ Random Value Guess Game Developer Silicon Brain }=========\n\n')
while(True):
    userValue = input('Enter a number in [10 to 99] in range | Type exit for quit :\n')

    if(userValue == randomValue):
        os.system('clear')
        print('\n\n ***[ WooHoo You Are Winner ]***\n')
        break;
    elif(userValue == 'exit'):
        break;
    elif(userValue >= randomValue):
        print('###--{ Your Number Is So Bigger }--###')
    elif(userValue <= randomValue):
        print('###--{ Your Number Is Son Smoller }--###')
    else :
        break;

print('___________________________\n')
print('| The Random Value Is : |\n')
print(randomValue)

with open('score.txt', 'a') as f:
    print(f.write(randomValue+'\n'))