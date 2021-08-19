def power_function(base, power):
    result = 1
    for i in range(power):
        result *= base

    return result


def main():
    base = int(input("Enter the base number :"))
    power = int(input("Enter the power number :"))
    print(f"The number {base} raised to the power {power} is: " +
          str(power_function(base, power)))

if __name__ == '__main__':
    main()