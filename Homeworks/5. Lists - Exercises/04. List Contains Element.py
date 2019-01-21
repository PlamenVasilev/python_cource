number_list = list(map(int, input().split()))
search = int(input())

if number_list.count(search):
    print('yes')
else:
    print('no')
