def sum(x,y,z):
    return x + y + z

def main():
    x = int(input('Enter first of three numbers :'))
    y = int(input('Enter second of three numbers :'))
    z = int(input('Enter third of three numbers :'))

    print("The given numbers are : " + str(x) + " " + str(y) + " and " + str(z))
    print("The biggest of the given numbers is: " + str(sum(x,y,z)))

if __name__ == "__main__":
    main()