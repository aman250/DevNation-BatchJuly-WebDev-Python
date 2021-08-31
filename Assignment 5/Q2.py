test_str = str(input("Enter a Sentence : "))
vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] 
new_string = [] 
string_list = list(test_str) 
for char in string_list: 
    for char2 in vowels_list: 
        if char == char2: 
            new_string.append("g") 
            break
    else: 
        new_string.append(char) 
print("Afer replacing vowels with the specified character : ",''.join(new_string)) 