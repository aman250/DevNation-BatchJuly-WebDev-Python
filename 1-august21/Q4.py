# FACTORIAL OF A NUMBER
number = input("PLEASE ENTER A NUMBER: ")
factorial = 1
for number in range(1,int(number)+1):
    factorial=factorial*number

print("FACTORIAL OF THE " + str(number) + " is: " + str(factorial))

