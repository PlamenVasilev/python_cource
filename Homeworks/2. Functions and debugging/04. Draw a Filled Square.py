def print_side(length):
    print('-', end='')
    for c in range(1,length-1):
        print("-", end='')
    print('-')


def print_row(length):
    print('-', end='')
    for col in range(1, length-1):
        if col % 2:
            print('\\', end='')
        else:
            print('/', end='')
    print('-')

def print_square(num):
    cols = num*2
    print_side(cols)
    if num > 2:
        for row in range(2, num):
            print_row(cols)
    print_side(cols)

num = int(input())
print_square(num)