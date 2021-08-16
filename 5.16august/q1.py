def func(base, power):
    res = 1
    for i in range(power):
        res = res * base
    return res

b= int(input("Enter base number:"))
p= int(input("Enter power number:"))
print("Result= ", func(b, p))