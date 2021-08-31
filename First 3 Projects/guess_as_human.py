import random


def guess(ending_range):
    randNo = random.randint(1, ending_range)
    guess = 0
    while guess != randNo:
        guess = int(
            input('Enter a number between 1 and '+str(ending_range)+' :'))
        if guess > randNo:
            print('try again! your guess is too high')
        elif guess < randNo:
            print('try again! your guess is too low')

    print('yay! you won the game. You guessed '+str(randNo)+' correctly.')


guess(10)
