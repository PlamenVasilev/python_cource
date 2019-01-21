numbers_list = list(map(int, input().split()))
total_odd = 0
for num in numbers_list:
    if num%2 != 0:
        total_odd += 1

print(total_odd)