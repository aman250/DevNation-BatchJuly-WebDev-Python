print("\n\t\t\t\t---------Program to calculates average of all elements of the list----------")

my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
#To find the sum of elements of list
add=(sum(my_list))
print("The sum of all elements is:"+str(add))
#To find the length of list
length=len(my_list)
print("The length of given list is:"+str(length))
#to calculate the average
avg=add/length
print("The average of all elements of list is:"+str(avg))
#insert the element at specific index
my_list.insert(4,65)
print("After inserting new value at index 4 ,the updated list is="+str(my_list))
