# secret word that needs too be guessed.
word = "python"

# this is an emty value to store guessed value.
guesses =" "

# total chances are 10
chances = 10

print('******WELCOME TO HANGMAN******\nYou will have 10 chances to guess the correct word.')

hint='This is an Interpreted language.'
print("HINT: " + hint)

# while loop will run untill chances are less then 10
while chances > 0:
    # initialy failed count is 0
    failed = 0

    # iterate through each char in the secret word
    for char in word:
         # if the guessed character is right print that
        if char in guesses:
            print(char,end="")
        else:
            # otherwise print ---- and increase the failed counter
            print("_",end="")
            failed += 1

    '''if failed count is 0 then you won and 
    break the loop else keep asking for guesses'''

    if failed == 0:
        print('\nCongrats! You have won.')
        break
    else:
        guess=input('\nEnter guess: ')
        guesses+=guess

        if guess not in word:
            print('Wrong guess, try again')
            chances = chances-1
            print("Chances left " ,chances)

        if chances == 0:
            print("OOPS! Game Over.")