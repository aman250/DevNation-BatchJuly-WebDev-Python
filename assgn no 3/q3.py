print("Start entering numbers")
sum = 0
c = 0
while 1:
    num = int(input())
    c = c + 1
    sum = sum + num
    print("Press q when you are done ")
    m = input()
    if m == 'q':
        break

print("Average", sum / c)
print("Sum", sum)