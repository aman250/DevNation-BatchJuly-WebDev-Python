def calc_power(base, power):
    return pow(base, power)


def inputs():
    global base, power
    base = int(input("Enter the base number? "))
    power = int(input("Enter the power number? "))


base, power = None, None

inputs()
print(f"{base}^{power} = {calc_power(base, power)}")