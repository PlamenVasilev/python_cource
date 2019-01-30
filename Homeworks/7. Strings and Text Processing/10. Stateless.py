
while True:
    string1 = input()
    if string1 == 'collapse':
        break
    string2 = input()

    try_replace = True
    while try_replace:
        string1 = string1.replace(string2,'')
        if len(string2)>1:
            string2 = string2[1:-1]
        else:
            try_replace = False

    if len(string1):
        print(string1)
    else:
        print('(void)')
