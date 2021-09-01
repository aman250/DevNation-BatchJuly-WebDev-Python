#Question_02
print("Program to replace the vowel letters from sentence with the letter "
      "the H")

#function definition
def replace_vowels(string):
    count = 0
    for letter in string:
        if letter in vowels_list:
            count += 1
            string = string.replace(letter, "g")

    if count > 0:
        print("The sentence after replacing vowels with the letter g is: " + string)
    else:
        print("The sentence has no vowels ")


#input from user
string=input("Enter the sentence:")
# vowels list
vowels_list=['A','E','I','O','U','a','e','i','o','u']
#function calling
replace_vowels(string)











