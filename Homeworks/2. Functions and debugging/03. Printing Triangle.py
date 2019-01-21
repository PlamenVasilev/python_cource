def print_head(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(f"{col} ", end='')
        print()


def print_foot(num):
    for row in range(num, 0, -1):
        for col in range(1, row):
            print(f"{col} ", end='')
        print()


def print_triangle(num):
    print_head(num)
    print_foot(num)


num = int(input())
print_triangle(num)