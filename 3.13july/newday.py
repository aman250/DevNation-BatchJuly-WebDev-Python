a= int(input("Enter a number  "))

f = 1

if a < 0:
    print("Factorial cant defined for negative integer")
elif (a == 0):
    print("The factorial of 0 is 1")
else:
    while (a > 0):
        f = f * a

        a = a - 1


    print(f)