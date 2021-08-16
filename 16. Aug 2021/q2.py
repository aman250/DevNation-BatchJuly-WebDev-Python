def replace_vowels(sentence):
    vowels = "aeiou"
    for letter in sentence:
        if letter in vowels:
            sentence = sentence.replace(letter, 'g')
    return sentence


sentence = input("Enter a sentence of your choice").lower()
sentence = replace_vowels(sentence)
print(f"Replaced vowels: {sentence}")
