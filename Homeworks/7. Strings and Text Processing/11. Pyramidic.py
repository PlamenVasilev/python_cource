import re

rows_count = int(input())
rows = []

while rows_count > 0:
    row = input()
    rows.append(row)
    rows_count -= 1

found = ''
found_len = 0
for r in range(0, len(rows)):
    char_count = {}
    for char in rows[r]:
        if found:
            if r+1 < len(rows):
                search_len = found_len + 2
                search = char*search_len
                regex = '['+search+']{'+str(search_len)+'}'
                if re.search(regex, rows[r+1], re.IGNORECASE):
                    found = search
                    found_len = search_len
                    break
        else:
            if r + 1 < len(rows):
                if re.search('['+char+']{2}', rows[r+1], re.IGNORECASE):
                    found = char
                    found_len = 3
                    break

for r in range(0,int((found_len+1)/2)):
    if r == 0:
        print(found[0])
    else:
        print(found[0] * ((r*2)+1))
