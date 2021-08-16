def vowels_fuc(user_string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for word in user_string:
        if word in vowels:
            user_string = user_string.replace(word, "g")
    return user_string

print("\n\t\t\t\t\t******************************************  ****************************************** \n\t\t\t\t\t"
                  "                                          Q2                                          \n\t\t\t\t\t"
                  "******************************************  ******************************************")
customer_senetence=input("\n\t\t\t\t\tEnter the sentence/paragraph: ")
print("\n\n\t\t\t\t\tThe sentence after replacing vowels with the letter \"g\" is: \n\n\t\t\t\t\t"
      "\t\t\t\t\t\t",vowels_fuc(customer_senetence))