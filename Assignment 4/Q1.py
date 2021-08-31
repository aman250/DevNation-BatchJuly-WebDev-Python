def MAX(x,y,z):
    largest = 0
    if x>y and x>z:
        largest=x
    elif y>x and y>z:
        largest=y
    else:
        largest=z
    return(largest)
print(MAX(4,3,9))