#program to Calculate the average

count=0
sum=0
product=1
#this loop will run infinity times
while True:
    num = int(input("Enter an integer input:"))
    sum = sum + int(num)
    product = product * num
    print("Enter q if you want to quit or press Enter to continue")
    more=input("")
    count = count + 1
    if more=="q":
        break
average=sum/count
print("Toatl number of times you entered the integer value is:",count)
print("The average of numbers is:",average)
print("The product of numbers is:",product)

