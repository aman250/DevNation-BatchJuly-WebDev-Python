# AVERAGE OF LIST ALSO ADD A VALUE IN INDEX 4
my_list = [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
average = sum(my_list)/len(my_list)
print("AVERAGE OF THE LIST IS: " + str(average))

my_list.insert(4,65)
print(my_list)