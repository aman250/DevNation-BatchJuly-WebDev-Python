# Q3 >>> Hangman game

# word that needs too be guessed.
word = "python"

# this is an empty variable to store a guessed value.
guesses = " "

# total chances are 10
chances = 10

print('WELCOME TO HANGMAN\nYou will have 10 chances to guess the correct word.')

# while loop will run until chances are less then 10
while chances > 0:
    failed = 0

    # iterate through each char in the secret word
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
