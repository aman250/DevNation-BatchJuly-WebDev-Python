# Question_02
print("\n\t\t\t\t--------------------Program to take sum of number using function--------------\n\n")

# function definition for addition
def add(num1, num2, num3):
    result = num1+num2+num3
    return result

# main part of Program
num1 = int(input("Enter first number:"))  # enter num1 for addition
num2 = int(input("Enter second number:"))  # enter num2 for addition
num3 = int(input("Enter third number:"))  # enter num2 for addition
print("The addition of three numbers is: "+str(add(num1, num2, num3)))   #function calling and printing the return result by function


