num = int(input("Enter a Number: "))

i=1
while i<=num:
  j=1
  while j<=i:
    print("*", end="")
    j+=1
  print("")
  i+=1