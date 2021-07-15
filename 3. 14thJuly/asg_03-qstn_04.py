#program to calculate the average of following list

my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

sum=0

#loop to find the sum of list
for num in my_list:
    sum=sum+num
print("The sum of given list is:",sum)

#to find the length of list
length=len(my_list)
print("The length of give list is:",length)

#Calculate Average
average=sum/length
print("The average of given list is:",average)
