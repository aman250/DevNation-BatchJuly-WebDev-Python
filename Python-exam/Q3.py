value = "Hello"
guess = ""
guess_limit = 10
guess_count = 0
guess_over = False

while guess != value:
    if guess_count<guess_limit:
       guess = input("please enter the value: ")
       guess_count = guess_count + 1
    else:
        guesses_over = True

if guess_over:
    print("Oops game over! You have not guess the correct value")
else:
    print("You Won!")