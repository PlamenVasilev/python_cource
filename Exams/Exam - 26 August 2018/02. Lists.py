while True:
    data = input()
    if data == 'stop playing':
        break

    int_list = list(map(int, data.split()))
    if len(int_list) == len(set(int_list)):
        int_list = list(map(lambda x: x+2 if not x%2 else x , int_list))
        print(f'Unique list: '+(",".join(map(str, sorted(int_list)))))
        list_sum = sum(int_list)/len(int_list)
        print(f'Output: {list_sum:.2f}')
    else:
        int_list = list(map(lambda x: x + 3 if x % 2 else x, int_list))
        print(f'Non-unique list: ' + (":".join(map(str, sorted(int_list)))))
        list_sum = sum(int_list)/len(int_list)
        print(f'Output: {list_sum:.2f}')
