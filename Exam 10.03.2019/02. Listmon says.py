listmon = list(map(int, input().split()))

rounds = 0
while True:
    data = input().split()
    command = data[0]

    if command == 'set':
        if len(listmon) == len(set(listmon)):
            print("It is a set")
        else:
            print(sorted(set(listmon), key=listmon.index))

    elif command == 'filter':
        filter_type = data[1]
        if filter_type == 'odd':
            odd_list = [x for x in listmon if x % 2 > 0]
            if len(odd_list):
                print(odd_list)
        elif filter_type == 'even':
            even_list = [x for x in listmon if x % 2 == 0]
            if len(even_list):
                print(even_list)

    elif command == 'multiply':
        multiplier = int(data[1])
        print([x*multiplier for x in listmon])

    elif command == 'divide':
        devider = int(data[1])
        if devider != 0:
            print([(x/devider) for x in listmon])
        else:
            print("ZeroDivisionError caught")

    elif command == 'slice':
        slice_from = int(data[1])
        slice_to = int(data[2])
        if max(slice_from,slice_to) >= len(listmon):
            print('IndexError caught ')
        else:
            print(listmon[slice_from:slice_to+1])

    elif command == 'sort':
        print(sorted(listmon))

    elif command == 'reverse':
        print(list(reversed(listmon)))

    elif command == 'exhausted':
        print(f'I beat It for {rounds} rounds!')
        break

    rounds += 1
