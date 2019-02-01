import re
string = input()

while True:
    command = input()

    if command == 'end':
        print(string)
        break
    else:
        command, arg1, arg2 = re.match(r'^(Insert|Delete|Left|Right)\s(\d+)\s?(\d+|\w+)?\s?', command).groups()
        if command == 'Insert':
            string = string[:int(arg1)]+arg2+string[int(arg1):]
        elif command == 'Delete':
            string = string[:int(arg1)]+string[int(arg2)+1:]
        elif command == 'Left':
            move = int(arg1) % len(string)
            string = string[move:]+string[:move]
        elif command == 'Right':
            move = int(arg1) % len(string)
            string = string[-move:]+string[:-move]
