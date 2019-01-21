string_list = input().split()
last = string_list.pop()
string_list.insert(0, last)

print(' '.join(string_list))
