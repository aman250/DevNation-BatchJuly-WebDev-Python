def power(base, expo):
    res = 1
    for i in range(expo):
        ans = base ** expo
        return ans


b = int(input("enter a base number..: "))
e = int(input("enter a power number...: "))
print(power(b, e))
