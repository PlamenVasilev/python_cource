travel_dict = {}
travellers = {}

while True:
    data = input()

    if data == 'ready':
        break

    city = data.split(':')[0]
    info_list = data.split(':')[1].split(',')

    if city not in travel_dict:
        travel_dict[city] = {}

    for info in info_list:
        type = info.split('-')[0]
        capacity = info.split('-')[1]
        travel_dict[city][type] = int(capacity)


while True:
    data = input()

    if data == 'travel time!':
        break

    destination = data.split()[0]
    people = int(data.split()[1])

    available = sum(travel_dict[destination].values())
    if people <= available:
        print(f'{destination} -> all {people} accommodated')
    else:
        print(f'{destination} -> all except {people - available} accommodated')
