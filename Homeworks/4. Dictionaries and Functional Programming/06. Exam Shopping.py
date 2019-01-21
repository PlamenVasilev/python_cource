dict = {}

action = 'stock'

while True:
    inp = input()
    if inp == 'shopping time':
        action = 'buy'
        continue
    elif inp == 'exam time':
        for key, val in dict.items():
            if val>0:
                print(f'{key} -> {val}')
        break

    (do, product, quantity) = inp.split(' ')

    if action == 'stock':
        if product in dict:
            dict[product] += int(quantity)
        else:
            dict[product] = int(quantity)
    elif action == 'buy':
        if product in dict:
            if dict[product] >= int(quantity):
                dict[product] -= int(quantity)
            elif dict[product] == 0:
                print(f"{product} out of stock")
            else:
                dict[product] = 0
        else:
            print(f"{product} doesn't exist")

