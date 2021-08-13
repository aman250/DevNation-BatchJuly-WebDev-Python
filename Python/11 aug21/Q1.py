def max_function(num1,num2,num3):
  max=1
  if num1 > num2 and num1 > num3:
    max = num1
  elif num2 > num3 and num2 > num1:
    max = num2
  elif num3 > num1 and num3 > num2:
    max = num3
  print(max)  

max_function(3,8,6)
  

