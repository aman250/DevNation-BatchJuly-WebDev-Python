# question_01
print("Program to check the maximum number using function")

# function definition
def max_num(num1, num2, num3):
    if(num1 > num2) and (num1 > num3):
        return num1
    elif(num2 > num1) and (num2 > num3):
        return num2
    else:
        return num3


# Program's main body
maximum = max_num(15, 55, 79)  #function calling and storing the return value by function
print("The maximum number among the three given number is " + str(maximum))
