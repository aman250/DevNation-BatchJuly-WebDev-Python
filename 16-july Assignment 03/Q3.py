numbersList = []
inputValue = " "
product = 1

while inputValue != "q":
    inputNumber = int(input("Enter the value:"))
    numbersList.append(inputNumber)
    inputValue = input("Press q for exit and press any number to proceed: ")

for i in range(0,len(numbersList)):
    product*=numbersList[i]
print("The product of input Numbers is: " + str(product))
average=sum(numbersList) / len(numbersList)
print("Average of the list is: "+str(average))