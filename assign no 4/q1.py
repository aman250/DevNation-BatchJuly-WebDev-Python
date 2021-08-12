#Write a function that has three numbers as a parameter and checks the maximum number among the three parameter numbers given and returns the value of the maximum number.
def maximum(a,b,c):
    list = (a,b,c)
    return max(list)

a = 14
b = 12
c= 14
print(maximum(a ,b,c))