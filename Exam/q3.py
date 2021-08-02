# hangman-game
word = "Pakistan"

guesses = " "

chances = 10

print('#####-WELCOME TO HANGMAN-######')

print('You will have 10 chances to guess the correct word.')

while chances > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")
        else:

            print("_", end="")
            failed += 1



    if failed == 0:
        print('\nCongrats! You have won.')
        break
    else:
        guess = input('\nEnter guess: ')
        guesses += guess

        if guess not in word:
            print('Wrong guess, try again')
            chances = chances - 1
            print("Chances left ", chances)

        if chances == 0:
            print("OOPS! Game Over.")