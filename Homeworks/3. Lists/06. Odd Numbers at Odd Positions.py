numbers_list = list(map(int, input().split()))

for index in range(0, len(numbers_list)):
    if index%2 != 0 and numbers_list[index]%2 != 0:
        print(f"Index {index} -> {numbers_list[index]}")


