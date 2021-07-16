print("Factorial")
inputNumber = int(input("Enter the Number: "))
print(inputNumber)
factorial = 1
print("The factorial of " + str(inputNumber) + " is ")
while inputNumber >= 1:
    factorial = factorial*inputNumber
    inputNumber = inputNumber - 1

print(str (factorial))