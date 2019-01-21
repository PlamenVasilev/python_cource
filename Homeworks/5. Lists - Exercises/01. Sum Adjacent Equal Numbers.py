numbers_list = list(map(float, input().split()))

search = True
while search:
    search = False

    for index in range(0, len(numbers_list)):
        if index+1 < len(numbers_list):
            if numbers_list[index] == numbers_list[index+1]:
                numbers_list[index] += numbers_list[index+1]
                numbers_list.pop(index+1)
                search = True
                break

print(" ".join(map(str, map("{:g}".format, numbers_list))))