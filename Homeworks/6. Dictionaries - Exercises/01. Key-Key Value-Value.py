the_key = input()
the_value = input()
the_n = int(input())

for n in range(0, the_n):
    search_key, search_values = input().split(' => ')
    if the_key in search_key:
        print(f'{search_key}:')
        for sub_key in search_values.split(';'):
            if the_value in sub_key:
                print(f'-{sub_key}')

