def removeVowels(sentence,):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in sentence:
        if c in vowels:
            res = sentence.replace(c,"g")
    return res

sentence= input("Enter your sentence: ")
print("replacing vowels with letter g: " +removeVowels(sentence))