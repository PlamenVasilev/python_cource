text = input()
separators = [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[', ']','?']

for s in separators:
    text = text.replace(s, ' ')
word_list = filter(None, text.split(' '))

lower_lits = []
mixed_list = []
upper_list = []

for word in word_list:
    lower_chars = 0
    upper_chars = 0

    for char in word:
        if char.islower():
            lower_chars += 1
        if char.isupper():
            upper_chars += 1

    if len(word) == lower_chars:
        lower_lits.append(word)
    elif len(word) == upper_chars:
        upper_list.append(word)
    else:
        mixed_list.append(word)

print('Lower-case: ' + (", ".join(lower_lits)))
print('Mixed-case: ' + (", ".join(mixed_list)))
print('Upper-case: ' + (", ".join(upper_list)))
