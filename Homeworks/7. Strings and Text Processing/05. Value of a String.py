string = input()
case = input()

if case == 'UPPERCASE':
    print('The total sum is: ' + str(sum(ord(ch) for ch in string if ch.isupper())))

if case == 'LOWERCASE':
    print('The total sum is: ' + str(sum(ord(ch) for ch in string if ch.islower())))
