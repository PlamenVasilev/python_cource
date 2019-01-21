number_list = list(map(int, input().split()))
min_num = None

for num in number_list:
    if min_num == None:
        min_num = num
    elif num < min_num:
        min_num = num

print(min_num)