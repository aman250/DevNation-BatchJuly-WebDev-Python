def main():
    sentence = str(input("Enter a sentence :"))
    print('The sentence you entered is :\n' + sentence)
    for letter in 'aeiouAEIOU':
        sentence = sentence.replace(letter,'g')
        
    print('The sentence after the operation is :\n' + sentence)


if __name__ == "__main__":
    main()
