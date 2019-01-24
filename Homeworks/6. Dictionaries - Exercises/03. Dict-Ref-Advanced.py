data = input()
dict_ref = {}

while not data == 'end':
    key = data.split(' -> ')[0]
    value = data.split(' -> ')[1]

    if value in dict_ref:
        dict_ref[key] = dict_ref[value].copy()
    else:
        try:
            values = list(map(int, value.split(', ')))
            if key not in dict_ref:
                dict_ref[key] = values
            else:
                dict_ref[key].extend(values)
        except:
            pass

    data = input()


for key, val in dict_ref.items():
    print(f'{key} === {", ".join(list(map(str, val)))}')
