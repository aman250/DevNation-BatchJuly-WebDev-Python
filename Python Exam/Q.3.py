Para = "Join the Conversation Follow our blog and social media channels for product tips, how-to guides, company updates, and more"
space_para = "Join the ___ Follow our blog and social ___ channels for product tips, how-to guides, ___ updates, and more"
guess_words = ["conversation", "media", "company"]
print("\t\t\t Welcome to HangMan Game\n\n")
print("Guess THis para words: \n\tNote:\n\t\tYou Have Only 10 lifes")
print("\n\t\t\t\t The Para is \n", space_para)
total_life = 10
guess_count: int = 1
em_lst = []
guesses = False
print("Enter Your Guesses:")
while guess_count<total_life:
    guess = input()
    em_lst.append(guess)
    guess = input()
    em_lst.append(guess)
    guess = input()
    em_lst.append(guess)
    if em_lst == guess_words:
        guesses = True
        break
    else:
        print("Guesses Again!")
        em_lst.clear()
        guess_count += 1
if guesses:
    print("Congratulations: you Won! ")
else:
    print("OOPS! You lose the game\n \t\tthe actual para was \n", Para)