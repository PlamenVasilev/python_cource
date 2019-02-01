string = input()

for char in sorted(set(string), key=string.index):
    print(char+":"+("/".join(map(str, [i for i, ltr in enumerate(string) if ltr == char]))))

