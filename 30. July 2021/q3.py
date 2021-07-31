############### Basic Version###############
import random

# TODO-1: - Update the word list to use the 'word_list'.
# Delete this line:
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"Word that we are guessing: {chosen_word}")

end_of_game = False
lives = 10

# TODO-2: verify user make right or wrong guess

while lives > 0 and not end_of_game:
    guess = input("Make a guess of any alphabet:? ")
    if guess not in chosen_word:
        print("Your guess is incorrect")
        lives -= 1
        print(f"Lives: {lives}")
    else:
        for character in chosen_word:
            if character == guess:
                chosen_word = chosen_word.replace(character, "")

                print(f"Remaining word: {chosen_word}")

    if len(chosen_word) == 0:
        print("“Congrats! You have won.”")
        end_of_game = True

    if lives == 0:
        end_of_game = True
        print("“OOPS! Game Over.”")





