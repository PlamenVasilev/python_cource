string = input()
string_list = [x for x in string]
counts = {}

for letter in string_list:
    cnt = string_list.count(letter)
    counts[letter] = cnt

for key, val in counts.items():
    print(f"{key} -> {val}")
