inventory_list = input().split()

while True:
    data = input()
    if data == 'Fight!':
        print(" ".join(inventory_list))
        break

    command = data.split()[0]
    equipment = data.split()[1]

    if command == 'Buy':
        if equipment not in inventory_list:
            inventory_list.append(equipment)
    elif command == 'Trash':
        if equipment in inventory_list:
            inventory_list.remove(equipment)
    elif command == 'Repair':
        if equipment in inventory_list:
            eq = inventory_list.pop(inventory_list.index(equipment))
            inventory_list.append(eq)
    elif command == 'Upgrade':
        try:
            eq, up = equipment.split('-')
            if eq in inventory_list:
                index = inventory_list.index(eq)
                inventory_list.insert(index+1, eq+":"+up)
        except:
            pass
