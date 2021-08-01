value = input("enter a hidden value: ")
print("remember your hidden value is ", value)
guess = ''
guess_limit = 10
guess_count = 0
guesses_over = True
while guess != value:
    while guess_count < guess_limit:
        guess = input('enter value :')
        if guess == value:
            print("you Won! game over! and you've repeated", str(guess_count), "times.")
            exit()
        else:
            print("Wrong! try again")
        guess_count = guess_count + 1
    print(f'oops game over! and you try {guess_count} time')