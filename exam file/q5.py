### Calculate avg of all numbers
my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

# Calculating average
avg = round(sum(my_list) / len(my_list))

print("Average of given list is: ", avg)

# replaced the value at 4th index with 65
my_list[4]=65

print("The new list: ",my_list)