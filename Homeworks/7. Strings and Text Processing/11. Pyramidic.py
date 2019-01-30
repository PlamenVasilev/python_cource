rows_count = int(input())
rows = []

while rows_count > 0:
    row = input()
    rows.append(row)
    rows_count -= 1

last_row = rows.pop()

char_count = {}
for char in set(last_row):
    char_count[char] = last_row.count(char)

maxed = sorted(char_count, key=char_count.get, reverse=True)[0]
height = int((last_row.count(maxed)+1)/2)

for r in range(0,height):
    if r == 0:
        print(maxed)
    else:
        print(maxed * ((r*2)+1))

