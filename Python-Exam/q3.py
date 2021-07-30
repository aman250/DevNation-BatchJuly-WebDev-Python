word = "python"
guesses =""
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print('You guessed it right: ',char,end="")
        else:
            print("_",end=" ")
            failed += 1
        if failed==0:
            print('Congrates. You won')
        else:
            guess=input('\nEnter guess')
            guesses+=guess
            if guess not in word:
                print('Wrong guess')
                turns-=1
                print("Chances left ",turns)

                if turns==0:
                    print("OOPS! Game Over.")


