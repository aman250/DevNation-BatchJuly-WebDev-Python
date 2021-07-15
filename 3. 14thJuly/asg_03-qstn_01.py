#program to find the Factorial of a number
fact=1
num=int(input("Enter number for finding factorial:"))
if num==0:
    print("The factorial of 0 is 1")
else:
    while num>=1:
        fact=fact*num
        num=num-1
print("The factorial of given number is "+str(fact))
