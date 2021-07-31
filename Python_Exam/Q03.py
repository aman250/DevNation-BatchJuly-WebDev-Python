import random

print("Welcome to Hangman Game")
words = ["python", "javascript","reactjs","nodejs"]
guess_limit = 10
real_word = words[random.randrange(len(words))]
input_letter = []
while guess_limit > 0:
    guess = input("Enter the letter: ")
    if real_word.__contains__(guess):
        print("You Entered the correct word go ahead ->")
        input_letter.append(guess)
        if input_letter.__len__() == real_word.__len__():
            print("Congrats! You have won.")
            break
        else:
            lettersleft = real_word.__len__() - input_letter.__len__()
            print("You have " ,lettersleft, "words left")

    else:
        guess_limit -= 1
        if guess_limit == 0:
            print("“OOPS! Game Over")
        else:
            print("You have",guess_limit,"tries left")









