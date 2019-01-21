def multiply(num, mul):
    return num*mul


string_list = list(map(int, input().split()))
multiplier = int(input())
number_list = [multiply(el, multiplier) for el in string_list]
print(' '.join(list(map(str, number_list))))
