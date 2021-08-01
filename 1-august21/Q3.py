# write program to build hangman game
import random

wordlist = ["simple","coding","english","mobile","cricket","tea","football","covid","pakistan","laptop","engineering","pen","chairs"]
word_chosen = ""

max_guesses = 10
current_guesses_counter = 0
letters_guessed = []
current_guess = ""
n=1
while True:
    word_chosen = random.choice(wordlist)
    letters_guessed = len(word_chosen) * "_"
    current_guesses = 0

    print("Welcome to hangman!")
    print("This word is ", len(letters_guessed), " letters")

    while current_guesses_counter < max_guesses:
        current_guess = input("Enter a letter: ")
        for i in range(0, len(word_chosen)):

            if word_chosen[i] == current_guess:
                letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i+1:]
                print(letters_guessed)

        if word_chosen == letters_guessed:
            print("Congrats! You guess the first word. Now guess the second word.")
            word_chosen = random.choice(wordlist)
            letters_guessed = len(word_chosen) * "_"
            current_guesses = 0

            print("Welcome to hangman!")
            print("This word is ", len(letters_guessed), " letters")

            while current_guesses_counter < max_guesses:
                current_guess = input("Enter a letter: ")
                for i in range(0, len(word_chosen)):

                    if word_chosen[i] == current_guess:
                        letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i + 1:]
                        print(letters_guessed)

                if word_chosen == letters_guessed:
                    print("Congrats! You guess the second word. Now guess the third word.")
                    word_chosen = random.choice(wordlist)
                    letters_guessed = len(word_chosen) * "_"
                    current_guesses = 0

                    print("Welcome to hangman!")
                    print("This word is ", len(letters_guessed), " letters")

                    while current_guesses_counter < max_guesses:
                        current_guess = input("Enter a letter: ")
                        for i in range(0, len(word_chosen)):

                            if word_chosen[i] == current_guess:
                                letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i + 1:]
                                print(letters_guessed)

                        if word_chosen == letters_guessed:
                            print("Congrats! You have won")
                            exit()

        current_guesses_counter+=1

    print("OOPS! Game Over")
    exit()