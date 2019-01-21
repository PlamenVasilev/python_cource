users = {}
action = 'collect'
unsuccessful = 0

while True:
    inp = input()
    if inp == 'login':
        action = inp
        continue
    elif inp == 'end':
        print(f'unsuccessful login attempts: {unsuccessful}')
        break

    (username, password) = inp.split(' -> ')
    if action == 'login':
        if username in users and users[username] == password:
            print(f'{username}: logged in successfully')
        else:
            print(f'{username}: login failed')
            unsuccessful+=1

    else:
        users[username] = password

