def avg_function(avg):
  sum = 0
  count = 0
  for x in avg:
    sum = sum + x
    count+=1
  average = sum/count
  return average


def check_function(check):
  if  (check % 2 == 0):
    print("The Number is EVEN")
  else:
    print("The Number is ODD")



nums = [1,2,3,4,5,6,7,8,9]
avgnum = avg_function(nums)
print(avgnum)
check_function(avgnum)