# printing right triangle
for i in range(1, 5):
    for j in range(i):
        print('*', end='')
    print('')


# printing diamond
stop = 1
ignore = True
flag = True
for i in range(-5, 6, 2):
    # calculating the limit for internal loop printing spaces
    internal_stop = int((abs(i)-1)/2)
    # skipping the printing of extra line
    if internal_stop == 0:
        if ignore:
            ignore = False
            continue
    # loop to print spaces
    for j in range(0, internal_stop):
        print(" ", end="")
    # loop to print *
    for k in range(stop):
        print("*", end="")
    print("")
    # reversing the limiting point for * printing loop
    if stop < 5:
        if flag:
            stop += 2
        else:
            stop -= 2
    else:
        stop -= 2
        flag = False


# prining reverse pyramid of 1,0
for i in range(1, 8, 2):
    # loop to print spaces
    for j in range(int(i/2)):
        print(" ", end="")
    # loop to print 1,0
    for k in range(8 - i):
        if k % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print("")
