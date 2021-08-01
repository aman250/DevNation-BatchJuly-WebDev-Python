#Q5 Python Exam

print("\n\t\t\t\t\t Average of all Elements of \n\t\t\t\t\t\t\t Array List")
my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
addition_of_myList=0
for i in my_list:
    addition_of_myList +=i
print("\n\t\t\t Average of list is ",addition_of_myList/len(my_list),"\n\t\t\t Where"
                " sum of list is ",addition_of_myList,"\n\t\t\t and length of "
                            "list is ",len(my_list))

print("\n\n\t\t\t Inserting the index Number 4  with 65")
# temp=my_list[4]
# my_list[4]=65
my_list.insert(4,65)
print("\n\nUpdated list is now ",my_list,"\n\n\t\t\t\t\t\t Code By Haseeb Rehman\n\n\t\t\t\t\t\t\t\t********")