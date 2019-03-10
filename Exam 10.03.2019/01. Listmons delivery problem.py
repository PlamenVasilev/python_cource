width = float(input())
depth = float(input())
height = float(input())

truck_area = width*height*depth

number_of_barels = int(input())

loaded_barels = 0
truck_full = False
for b in range(0,number_of_barels):
    barel_radius = float(input())
    barel_height = float(input())

    barel_area = 3.141592653589793*barel_radius*barel_radius*barel_height

    if truck_area-barel_area > 0:
        truck_area = truck_area-barel_area
        loaded_barels += 1
    else:
        print(f'Truck is full. {loaded_barels} on board!')
        truck_full = True
        break

if not truck_full and truck_area > 0:
    print(f"All barrels on board. Capacity left - {truck_area:.2f}.")

