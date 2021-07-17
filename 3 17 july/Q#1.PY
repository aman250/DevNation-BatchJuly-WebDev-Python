#calculate factorial

num=int(input("enter number whose factorial needs to be known:"))

fact=1

if num==0 or num==1:
    print(1)
elif num<0:
    print("factorial doesn't exist")
else:
    for i in range(1, num+1):
        fact=fact*1
        print("factorial of", num,"is",fact)