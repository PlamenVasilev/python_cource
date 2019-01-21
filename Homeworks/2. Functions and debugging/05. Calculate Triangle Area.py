def area_of_triangle(a, b):
    return (a*b)/2


a = float(input())
b = float(input())
area = area_of_triangle(a, b)

print(f'{area:.12g}')