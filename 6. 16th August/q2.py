
def convertVowels(sentence):
    index = 0
    for character in sentence:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            sentence = sentence[0:index]+'g'+sentence[index+1:]
        index += 1
    return sentence


inputSentence = input('Enter sentence:')
print(convertVowels(inputSentence))
