print("Enter the numbers You want to calculate the average:")
print("Press Q/q if you want Quit:")
sum = 0
count=0
product = 1
a=1
while a==1:
    num = int(input("Enter a number: "))
    sum = sum + num
    product = product * num
    count+=1
    str = input("Press Q/q for quit or Y/y for continue: ")
    if str == "Q" or str == "q":
      break
    elif str=="y" or str=="Y":
      continue
print("The average of all the numbers is: ",sum/count)
print("The product of the numbers is: ", product)