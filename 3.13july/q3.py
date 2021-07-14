print(" enter numbers")
add = 0
a = 0
while 1:
    n = int(input())
    a = a + 1
    add = add + n
    print(" Ask to press q to quit after every integer input")
    b = input()
    if b == 'q':
        break

print("Average", add / a)
print("add", add)