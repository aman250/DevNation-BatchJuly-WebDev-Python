import math
total = 0
more = True
values = []
while more:
    value = input("Enter the input press q to quit")
    if value == 'q':
        more = False
    else:
        values.append(int(value))

print(sum(values)/len(values))