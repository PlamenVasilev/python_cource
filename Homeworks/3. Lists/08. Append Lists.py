list_of_lists = input().split('|')
list_of_lists.reverse()
main_list = []

for l in list_of_lists:
    main_list.extend(l.split())

print(' '.join(map(str, main_list)))




