def power(base, exponent):
    result = base
    for i in range(1, exponent):
        result *= base
    return result


base = int(input("Enter a number: "))
exponent = int(input(f"Enter the power to which {base} is to be raised: "))
result = power(base, exponent)
print (f"{base} raised to the power {exponent} is {result}")