inputNumber = int(input("Enter the Number Whose factorial who want to find: "))
print(inputNumber)
fact = 1
for i in range(1, inputNumber + 1):
    fact = fact * i

print("The factorial of ", inputNumber, " is: ", fact)








