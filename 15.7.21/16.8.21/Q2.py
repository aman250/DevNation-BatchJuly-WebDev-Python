## function to replace vowels  with 'g'
def replace_vowel(sentence, letter="g"):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        sentence=sentence.replace(i,letter)
    return sentence




sentence=input('Enter any Sentence: ')
print("Replaced  vowels with 'g': "+ replace_vowel(sentence))