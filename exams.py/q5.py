#first of all we take average of array liat

def averageOfList(num):
    sumOfNumbers = 0
    #for t in num:
   #     sumOfNumbers = sumOfNumbers + t

  #  avg = sumOfNumbers / len(num)
 #   return avg

#print("The average of List is", averageOfList([1,22,32,12,55,88,,76,54,2,1,22,33,44,5,6,7,5,0]))


number_list = [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,7,5,0]
avg = sum(number_list)/len(number_list)
print("The average is ", round(avg,2))

number_list.insert(4,[65])
