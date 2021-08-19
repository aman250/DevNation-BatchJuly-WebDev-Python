def base_power(base, power):
    result = 1
    for i in range(power):
        result = result * base
    print("The result is:", result)


base_power(2, 3)