# question_01
print("\n\t\t\t\t--------------------Program to check the maximum number using function--------------\n\n")

# function definition
def max_num(num1, num2, num3):
    if(num1 > num2) and (num1 > num3):
        return num1
    elif(num2 > num1) and (num2 > num3):
        return num2
    else:
        return num3


# Program's main body
maximum = max_num(7, 34, 19)  #function calling and storing the return value by function
print("The maximum number among the three given number is " + str(maximum))


