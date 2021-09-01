#
print("Program to find the power of given number")

# function definition
def power(base_num, power_num):
    result = 1
    #power_num as passed as an argument to iterate the loop for that number of times
    for i in range(power_num):
        result = result*base_num
    print("The power of "+str(base_num)+" is: "+str(result))



#user defined Inputs
num1=int(input("Enter the base to find power of that number:"))
num2=int(input("Enter the power value:"))

#function calling
power(num1, num2)
