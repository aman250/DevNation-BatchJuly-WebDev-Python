sentence = input("Enter the string: ")
print("The Sentence is: ", sentence)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in sentence:
    if i in vowels:
        print('g')
    else:
        print(i)