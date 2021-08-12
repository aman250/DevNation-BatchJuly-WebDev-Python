def max(x,y,z) -> int:
    print(x,y,z)
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

def main():
    x = int(input('Enter first of three numbers :'))
    y = int(input('Enter second of three numbers :'))
    z = int(input('Enter third of three numbers :'))

    print("The given numbers are : " + str(x) + " " + str(y) + " and " + str(z))
    print("The biggest of the given numbers is: " + str(max(x,y,z)))

if __name__ == "__main__":
    main()