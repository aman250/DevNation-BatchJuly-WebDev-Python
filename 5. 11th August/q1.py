def max(a,b,c):
    if b<=a and c<=a:
        return a
    if a<=b and c<=b:
        return b
    if a<=c and b<=c:
        return c

print(max(-11,-11,-1))