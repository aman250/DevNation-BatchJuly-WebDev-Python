### function to calc base and power
def calc_exponent(base,exponent):
    return base**exponent


base=int(input("Enter base: "))
power=int(input("Enter exponent: "))
print("Result is: ",calc_exponent(base,power))
