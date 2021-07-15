my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
avg = 0
count=0 
for x in my_list:
  avg = avg + x
  count+=1
print("Average of the whole list is: ", avg/count)