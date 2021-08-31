def Avg(List):
    a = 0
    b = 0
    for x in List:
        a = x+a
        b = b + 1
    c = a/b
    return c
num = [1,3,5,4]
print(int(Avg(num)))
def evenodd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(evenodd(Avg(num)))