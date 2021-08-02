counter = 0
match_counter=0

print('Note: Please start guessing parts of the secret word. You can guess only single character and you have 10 guesses allowed!')
secret = 'win'
guess = ''

while(counter < 10):
    char = input('Enter character(lowercase):')
    guess+=char
    for x in guess:
        if x in secret:
            match_counter+=1
            if match_counter==len(secret):
                print('You guessed successfully!')
                break
    if match_counter==len(secret):
        break 
    counter = counter+1
    match_counter=0

if match_counter!=len(secret):
    print('You failed to guess within the alotted limit!')

