'''Write a program which asks a sentence from
the customer and when user enters the sentences then it checks
 for the vowels in that sentence and replace those vowels with a letter g.'''


### function to replace vowels in with 'g'
def replace_vowel(sentence, letter="g"):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        sentence=sentence.replace(i,letter)
    return sentence




sentence=input('Enter any Sentence: ')
print("Replaced  vowels with 'g': "+ replace_vowel(sentence))

