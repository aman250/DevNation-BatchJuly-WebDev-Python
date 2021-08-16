def replace(sen, g):
    vowel = "AEIOUaeiou"
    for i in vowel:
        sen = sen.replace(i, g)

    return sen


a = input("Enter any sentence:")
rep = "g"

print("Afer replacing vowels with the specified character:",
      replace(a, rep))
