my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
addition=0
#to calculate addition of all numbers for average
for i in range(0,len(my_list)):
    addition+=my_list[i]
print("Average of given  numbers in list  is",addition/len(my_list))