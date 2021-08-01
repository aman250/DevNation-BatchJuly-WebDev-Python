number = int(input("Enter the number you want the factorial of:"))
factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("The factorial of the number you entered is :" + str(factorial))


