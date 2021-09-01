# Question_03
print("Program that first find average of list elements then check the "
      "result for an even or odd number")

#function definition to find the average of list
def average(list):
    length = len(list)
    print("The length of given list is: "+str(length))
    add = 0
    for num in list:
        add = add+num
    print("The addition of given list elements is: "+str(add))
    return add/length


# function definition to find an even or odd number
def check_EvenOdd(value):
    if(value>=1):
        if(value%2==0):
            print("\nThe resultant value",value,"is even")
        else:
            print("\nThe resultant value",value,"is odd")
    else:
        print("The number is less then 1")

#main program
my_list = [8,4,2,0,1,5,7]
avg = average(my_list)  # function calling
print("The average of the given list elements is: ",avg)
print("Part 2")
check_EvenOdd(avg)  # function calling