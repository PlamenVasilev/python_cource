string = input()
case = input()

if case == 'UPPERCASE':
    print(sum(ord(ch) for ch in string.upper() if ch.isupper()))

if case == 'LOWERCASE':
    print(sum(map(ord, [ch for ch in string.lower() if ch.islower()])))
    print(sum(ord(ch) for ch in string.lower() if ch.islower()))
