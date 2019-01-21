number_list = list(map(int, input().split()))
number_list.sort(reverse=True)
cnt = int(input())

print(" ".join(map(str, number_list[:cnt])))