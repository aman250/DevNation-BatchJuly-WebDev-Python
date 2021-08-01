count = 10
condition = False
print("This game is called *******. I'm making it for my ****. Can you ***** the words hidden?")
print("Starting game...")
while count > 0 and condition == False:
    print(f"\nYou have {count} guesses remaining.")
    first_blank = input("Enter your guess for first blank space :")
    second_blank = input("Enter your guess for second blank space :")
    third_blank = input("Enter your guess for third blank space :")
    if first_blank == 'hangman' and second_blank == 'exam' and third_blank == 'guess':
        condition = True
        print("Congratulations! YOU WON!!!")
        break
    else: 
        print('Sorry! try again...\n\n\n')
        count -= 1

if count <= 0:
    print("Game Over!")