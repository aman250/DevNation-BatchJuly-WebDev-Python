my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
sum = 0
count = len(my_list)

for i in range(count):
    sum += my_list[i]

print("The average of the lis is: " + str(sum/count))