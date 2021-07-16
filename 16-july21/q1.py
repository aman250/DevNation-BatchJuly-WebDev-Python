n= int(input("Please enter your number: "))
i=1
fact=1
while n>0:
    fact=fact*n
    n=n-1

print("Factorial of the number is: " + str(fact))