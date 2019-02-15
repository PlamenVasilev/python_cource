import math

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

num_helmets = math.floor(lost_fights_count/2)
num_swords = math.floor(lost_fights_count/3)
num_shields = math.floor(lost_fights_count/6)
num_armors = math.floor(num_shields/2)

expenses = (num_helmets*helmet_price)+(num_swords*sword_price)+(num_shields*shield_price)+(num_armors*armor_price)

print(f'Gladiator expenses: {expenses:.2f} aureus')
