list_strings = input().split()
list_strings = [str.lower() for str in list_strings]
counts = {}

for string in list_strings:
    cnt = list_strings.count(string)
    counts[string] = cnt

print(", ".join([key for key, val in counts.items() if val%2 != 0]))