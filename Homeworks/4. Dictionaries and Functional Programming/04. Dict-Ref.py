dict = {}

while True:
    asdf = input()
    if asdf == 'end':
        break

    (key, val) = asdf.split(' = ')

    if val.isdigit():
        dict[key] = int(val)
    else:
        if val in dict:
            dict[key] = dict[val]

for key, val in dict.items():
    print(f"{key} === {val}")
