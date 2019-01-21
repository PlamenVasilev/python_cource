list_floats = list(map(float,input().split(' ')))
unique = {}

for number in list_floats:
    cnt = list_floats.count(number)
    unique[number] = cnt


for key, val in sorted(unique.items()):
    print(f'{key} -> {val} times')
