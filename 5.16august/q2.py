def replace(test_sen, g):
    vowels = "AEIOUaeiou"
    for i in vowels:
        test_sen = test_sen.replace(i, g)

    return test_sen

input_sen = input("Enter any sentence:")
rep = "g"

print("Afer replacing vowels with the specified character:",
      replace(input_sen, rep))
