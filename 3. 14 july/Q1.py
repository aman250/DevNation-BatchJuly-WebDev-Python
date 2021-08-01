a = int(input("enter number for factorial : "))
x = 1
b = 1
for i in range(a):
    x = x * b
    b = b + 1
print("Factorail of", a, "is : ", x)