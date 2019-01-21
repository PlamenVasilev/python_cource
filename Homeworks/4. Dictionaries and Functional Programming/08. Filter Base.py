ages = {}
salaries = {}
positions = {}

while True:
    prompt = input().strip()

    if prompt == 'filter base':
        show = input().strip()
        if show == 'Age':
            for key, val in ages.items():
                print(f'Name: {key}')
                print(f'Age: {val}')
                print('=' * 20)

        elif show == 'Salary':
            for key, val in salaries.items():
                print(f'Name: {key}')
                print(f'Salary: {val}')
                print('=' * 20)
        elif show == 'Position':
            for key, val in positions.items():
                print(f'Name: {key}')
                print(f'Position: {val}')
                print('=' * 20)

        break
    else:
        name, action = prompt.split(' -> ')

        try:
            if float(action) == int(float(action)):
                ages[name] = int(action)
            elif float(action) != int(float(action)):
                salaries[name] = float(action)
        except ValueError:
            positions[name] = str(action).strip()


        # try:
        #     ages[name] = int(action)
        # except:
        #     try:
        #         salaries[name] = float(action)
        #     except:
        #         try:
        #             positions[name] = str(action)
        #         except:
        #             pass

