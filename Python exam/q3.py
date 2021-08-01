# Q3 . Build a Hangman game using the while loop:
INPUT1 = '***'
INPUT2 = '***'
INPUT3 = '***'
INPUT4 = '***'
INPUT5 = '***'
INPUT6 = '***'
INPUT7 = '***'
INPUT8 = '***'
INPUT9 = '***'
INPUT10 = '***'
guess1 = 'quaid e azam'
guess2 = 'HOCKEY'
guess3 = 'Chukar '
guess4 = 'Markhor'
guess5 = 'Lady Finger'
guess6 = 'Mango'
guess7 = 'Gardenia'
guess8 = 'Mahseer'
guess9 = 'white'
guess10 = 'River Indus'
guess_limit = 10
guess_count = 0
guess_over = False

while guess1 != INPUT1 and guess2 != INPUT2 and guess3 != INPUT3 and guess4 != INPUT4 \
        and guess5 != INPUT5 and guess6 != INPUT6 and guess7 != INPUT7 and guess8 != INPUT8 \
        and guess9 != INPUT9 and guess10 != INPUT10 and not(guess_over):
    if guess_count < guess_limit:
        INPUT1 = input('Pakistan was founded by ___ ')
        INPUT2 = input('Pakistan national game___ ')
        INPUT3 = input('Pakistan national bird___ ')
        INPUT4 = input('Pakistan national ANIMAL___ ')
        INPUT5 = input('Pakistan national vegetable___ ')
        INPUT6 = input('Pakistan national fruit___ ')
        INPUT7 = input('Pakistan national FLOWER___ ')
        INPUT8 = input('Pakistan national Fish___ ')
        INPUT9 = input('Pakistan national colour___ ')
        INPUT10 = input('Pakistan national river___ ')
        guess_count = guess_count + 1
    else:
        guess_over = True

if guess_over:
    print('you lose the game')
else:
    print('won')