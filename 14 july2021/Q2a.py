num = int(input("Enter a Number: "))
#upper triangle
a=1
d=1
#lopp will run "num" times
while a<=num:
  b=1
  #will add empty spaces one less into "num" times
  while b<=num-a:
    print(" ",end="")
    b+=1
  c=1
  while c<=d:
    print("*", end="")
    c+=1
  print(" ")
  d+=2
  a+=1
  #lower triangle
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
    print('*', end = '')
    l+=1
  print(" ")
  i+=1