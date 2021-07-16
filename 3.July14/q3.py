num = int(input("Enter first number:"))
sum = 0
product = 1
count = 0
q = " "

flag = True
while q != "q" and q != "Q":
    print("\n")
    if not flag:
        num = int(input("Enter next number:"))
    flag = False
    sum += num
    product *= num
    count += 1
    q = str(input("Press 'q' to quit: "))

print("The average of the numbers you entered is: " + str(sum/count))
print("The product of all the numbers you entered is: " + str(product))
