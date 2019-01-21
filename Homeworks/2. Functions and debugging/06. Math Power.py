def calculate_power(a, b):
    return pow(a,b)


num = float(input())
power = int(input())

result = calculate_power(num, power)
print(f'{result}')