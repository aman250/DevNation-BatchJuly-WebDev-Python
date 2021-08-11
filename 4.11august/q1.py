def max(a, b, c) :
    m = a
    if a > b and a > c:
        m = a
    elif b > a and b > c :
        m = b
    else :
        m = c
    return m


print("Maximum number is=", max(1, 2, 3))