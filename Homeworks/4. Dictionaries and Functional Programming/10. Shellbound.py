import math

shells = {}
while True:
    data = input()
    if data == 'Aggregate':
        for region, data_list in shells.items():
            giant = math.ceil(sum(data_list) - (sum(data_list)/len(data_list)))
            shells_str = ", ".join(map(str, data_list))
            print(f'{region} -> {shells_str} ({giant})')
        break
    else:
        region, shell = data.split(' ')
        shell = int(shell)
        if region not in shells:
            shells[region] = []
        if shell not in shells[region]:
            shells[region].append(shell)
