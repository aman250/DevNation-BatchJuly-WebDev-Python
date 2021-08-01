#Q3 Python Exam
import random

print("\n\t\t\t\t\t\t\t\"Hangman \n\t\t\t\t\t\t\t\"Game\n")


print("\t Instruction:\n\t\t You Have Only \"10\" Guesses for the Whole Game\n\n")    #instruction about the game
guesses_allowed=10   # this variable is for user guesses
guesses_count=1  # this variable is counting the user life
para1="It had become a far too ___ an event in her life. " \
      "She has specifically placed the key to the box in a special place so that " \
      "she wouldn't ___ it and know exactly where it was when the key was needed. " \
      "Now that she needed to open the box, she had absolutely no idea where that " \
      "___ spot she placed the key might be."
para2="She ___ if the note had reached him. She scolded herself ___ not handing" \
      " it to him in person. She trusted her friend, but so much could happen. She waited " \
      "impatiently for ___."
para3="He picked up the ___ end of the branch and made a mark on the stone. Day 52 if " \
      "the marks on the stone were accurate. He couldn't be sure. Day and ___ had begun " \
      "to blend together ___ confusion, but he knew it was a long time. Much too long."
para4="He was aware there were numerous wonders of this ___ including the unexplained creations " \
      "of humankind that showed the wonder of ___ ingenuity. There are huge heads on Easter Island. " \
      "There are the Egyptian pyramids. There’s Stonehenge. But he now stood in front of a newly " \
      "___ monument that simply didn't make any sense and he wondered how he was ever going " \
      "to be able to explain it."
para5="MaryLou wore the tiara with ___. There was something that made doing anything she didn't " \
      "really want to do a bit easier when ___ wore it. She really didn't " \
      "care what those ___ through the window were thinking as she vacuumed her apartment."

hangman_blank_space_words=["common","lose","special","wondered","for","word","burnt","night","creating","world","our","discovered","pride","staring","she"]  #it contain the white spaces words

WORD=[para1,para2,para3,para4,para5]   # list for hangman game each time it take different para

HangMan=random.choice(WORD)  # herer the HangMan take the inputs from random function

print(HangMan)

guess_correct=False

print("\n\t\t\t Enter the Guess Words:_ \n")   #input prompt to user

while guesses_allowed>0:
    guess1 = input("\t\t\t")
    guess2 = input("\t\t\t")
    guess3 = input("\t\t\t")
    if hangman_blank_space_words.__contains__(guess1):
        if hangman_blank_space_words.__contains__(guess2):
            if hangman_blank_space_words.__contains__(guess3):
                guess_correct=True
                break
            else:
                guesses_allowed -=1
                print("You have ",guesses_allowed,"guesses left")
        else:
            guesses_allowed -= 1
            print("You have ",guesses_allowed,"guesses left")
    else:
        guesses_allowed -= 1
        print("You have ",guesses_allowed,"guesses left")

if guess_correct: #checking the user input string here
    print("\n\t\tCongrats! You have won ):","\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
else:
    print("\n\t\tOOPS! Game Over (:","\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t******** ")
