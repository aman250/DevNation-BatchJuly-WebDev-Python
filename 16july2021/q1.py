print("Factorial of any number n is represented by n! and is equal to 1*2*3*4...(n-1)")
n=int(input("please enter the number of n:"))
temp=1
while n>=1:
    temp*=n
    n=n-1
print(temp)

