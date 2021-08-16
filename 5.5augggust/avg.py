def find1(base, power):
    r = 1
    for i in range(power):
        r *= base

    return r

a = int(input("enter a base number"))
b = int(input("enter a power number"))
print(find1(a, b))
