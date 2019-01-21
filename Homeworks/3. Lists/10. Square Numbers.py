numbers_list = list(map(int, input().split()))
numbers_list.sort(reverse=True)
square_numbers = []

for num in numbers_list:
    if num > 0 and num**0.5 == int(num**0.5):
        square_numbers.append(num)


print(" ".join(map(str, square_numbers)))