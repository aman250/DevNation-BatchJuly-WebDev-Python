print("a.")
a = 1
while a <= 4:
    b = 1
    while b <= a:
        print("*", end=" ")
        b += 1
    print()
    a += 1

print("q2")
n = 3
i = 0
while i < n:
    j = 0
    k = 0
    while j < n-i:
        print(" ", end="")
        j += 1
    while k < 2*i+1:
        print('*', end="")
        k += 1
    i += 1
    print()
p ="*"
q ="*"
j = 0
k = 3
while k >= 1:
    print(" "*j + (k-1)*(p+q) +p+ " "*j)
    k = k-1
    j=j+1


print("q3")
p ="1"
q ="0"
j = 0
k = 3
while k >= 1:
    print(" "*j + (k-1)*(p+q) +p+ " "*j)
    k = k-1
    j=j+1





