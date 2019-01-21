dict = {}

while True:
    asdf = input()
    if asdf == 'Over':
        break

    (key, val) = asdf.split(' : ')

    if val.isdigit():
        dict[key] = str(val).strip()
    else:
        dict[val] = str(key).strip()

for key in sorted(dict):
    print(f"{key} -> {dict[key]}")
