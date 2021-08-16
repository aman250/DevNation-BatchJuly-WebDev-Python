def square(b,p):
  res = 1
  for i in range(p):
    res = res * b
    i+=1
  print(res)

base = int(input("Enter the Base number:"))
power = int(input("Enter the Power number:"))
square(base, power)