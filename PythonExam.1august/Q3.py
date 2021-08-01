print("Enter the hidden character (Ee_ha):")
val = "s"
guess = " "
turns = 10
count = 0
turns_over = False
if guess != val:
    while count < turns:
        guess = input('enter value :')
        if guess == val:
            print("you Won! and you've tried", str(count), "times.")
            exit()
        else:
            print("Wrong! try again")
        count = count + 1
    turns_over = True
if turns_over == True:
    print(f'oops game over! and you try {count} time')
    exit()

