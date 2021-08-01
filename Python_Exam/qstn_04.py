print("\n\t\t\t-----------Program to find Factorial of a number-------\n")
num=int(input("Enter the number to find factorial:"))
fact=1
if(num==0):
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*num
        num=num-1
    print("The factorial of number is:"+str(fact))
    #print("The factorial of"+str(num)+"is"+int(fact))
