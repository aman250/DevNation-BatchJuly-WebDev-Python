def averageOfList(numOfList):
    return sum(numOfList) / len(numOfList)

Avg= averageOfList([10,20,35,4,60,75,80,100,15,35])
print("The average of List is: " + str(Avg))

def even_odd(num):
    if num%2==0:
        print("the number is EVEN")
    else:
        print("the number is ODD ")
even_odd(Avg)
