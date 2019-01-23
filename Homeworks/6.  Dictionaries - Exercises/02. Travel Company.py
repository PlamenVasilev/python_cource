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
            type, capacity = info.split('-')
            travel_dict[city][type] = int(capacity)
    else:
        destination, people = data.split()

        if destination in travellers:
            travellers[destination] += int(people)
        else:
            travellers[destination] = int(people)

for city, people_count in travellers.items():
    available = sum(travel_dict[city].values())
    if people_count <= available:
        print(f'{city} -> all {people_count} accommodated')
    else:
        print(f'{city} -> all except {people_count - available} accommodated')
