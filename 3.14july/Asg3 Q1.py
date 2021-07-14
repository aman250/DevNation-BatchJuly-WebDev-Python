print("Claculating Factorial ")
fact_number=int(input("Please Enter a Number: "))
temp=1
while fact_number>=1:
    temp*=fact_number
    fact_number-=1
print(temp)