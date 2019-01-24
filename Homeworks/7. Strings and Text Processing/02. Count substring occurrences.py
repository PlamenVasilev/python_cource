string = input().lower()
search = input()
next = True
count = 0
start = 0

while next:
    index = string.find(search.lower(), start)
    if index != -1:
        start = index+1
        count += 1
    else:
        next = False

print(count)
