def print_greater(input, a,b):
    if input == 'int':
        a = int(a)
        b = int(b)
        print(max(a, b))
    else:
        print(max(a, b))


type = input()
a = input()
b = input()
print_greater(type, a, b)