numbers_list = list(map(int, input().split()))
new_list = []

for num in numbers_list:
    if num > 0:
        new_list.append(num)

new_list.reverse()

if len(new_list):
    print(' '.join(map(str, new_list)))
else:
    print('empty')