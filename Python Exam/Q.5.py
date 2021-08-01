my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
addition =0
for i in my_list :
   addition =addition +i
print("average value is ",addition/len(my_list))

my_list.insert(4,65)
print("after insertion the value 65 on index 4 is \n ",my_list)