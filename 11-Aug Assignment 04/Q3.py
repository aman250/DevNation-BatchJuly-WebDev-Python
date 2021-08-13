ef find_Average(listNum):
    return sum(listNum)/len(listNum)

def find_even_odd(givenList):
    if givenList % 2 == 0:
        print("Average is even")
    else:
        print("Average is Odd")

givenList = [2,4,6,8,5,4]
average = find_Average(givenList)
print("Average of the given list is: ", average)

find_even_odd(average)