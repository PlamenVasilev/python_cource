number_list = list(map(int, input().split()))

counts = {}
for num in sorted(number_list):
    counts[num] = number_list.count(num)

for num, count in counts.items():
    print(f'{num} -> {count}')

