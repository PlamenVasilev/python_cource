import re

regex = r"name is\s([A-Z][a-z]+\s[A-Z][a-z]+).*?\s([0-9]{2})\syears.*?on\s(\d\d-\d\d-\d\d\d\d)\."

persons = []
while True:
    data = input()

    if data == 'make migrations':
        if len(persons):
            for person in persons:
                print(f'Name of the person: {person["name"]}.')
                print(f'Age of the person: {person["age"]}.')
                print(f'Birthdate of the person: {person["birth"]}.')
        else:
            print('DB is empty')
        break
    match = re.search(regex, data)
    if match:
        persons.append({
            'name': match.group(1),
            'age': match.group(2),
            'birth': match.group(3)
        })

