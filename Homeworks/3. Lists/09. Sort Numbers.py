numbers_list = list(map(int, input().split()))
numbers_list.sort()

print(" <= ".join(map(str, numbers_list)))