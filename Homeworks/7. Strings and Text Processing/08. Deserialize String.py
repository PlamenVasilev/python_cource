string = {}

while True:
    inp = input()
    if inp == 'end':
        print("".join( string[key] for key in sorted(string)))
        break
    else:
        char = inp.split(':')[0]
        for pos in inp.split(':')[1].split('/'):
            string[int(pos)] = char
