num = int(input("Enter a Number: "))
i=1
k=1
while i<=num-1:
  j=1  
  while j<=k:
    print(" ", end="")
    j+=1
  k+=1 
  l=1
  while l<=(2*(num-i)-1):
    if l%2==0:
      print("0", end="")
    else:
      print("1",end="")
    l+=1 
  print(" ")
  i+=1
    