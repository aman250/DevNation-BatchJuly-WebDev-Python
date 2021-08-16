def power(base, power_num):
    return pow(base, power_num)


def inputs():
    global base, power_num
    base = int(input("Enter the base number? "))
    power_num = int(input("Enter the power number? "))


base, power_num = None, None

inputs()
print(f"{base}^{power_num} = {power(base, power_num)}")
