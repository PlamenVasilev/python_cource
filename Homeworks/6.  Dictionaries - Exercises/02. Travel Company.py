travel_dict = {}
travellers = {}
phase_1 = True

while True:
    data = input()
    if data == 'travel time!':
        break

    if data == 'ready':
        phase_1 = False
        continue

    if phase_1:
        city = data.split(':')[0]
        info_list = data.split(':')[1].split(',')

        if city not in travel_dict:
            travel_dict[city] = {}

        for info in info_list:
            type = info.split('-')[0]
            capacity = info.split('-')[1]
            travel_dict[city][type] = int(capacity)
    else:
        destination = data.split()[0]
        people = data.split()[1]

        if destination in travellers:
            travellers[destination] += int(people)
        else:
            travellers[destination] = int(people)

for city, people_count in travellers.items():
    if city in travel_dict:
        available = sum(travel_dict[city].values())
        if people_count <= available:
            print(f'{city} -> all {people_count} accommodated')
        else:
            print(f'{city} -> all except {people_count - available} accommodated')
