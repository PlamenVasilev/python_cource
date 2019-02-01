import re

diamonds_string = input()

matches = re.findall(r'<(.*?)>', diamonds_string)
if len(matches):
    for match in matches:
        print(f'Found {sum(int(d) for d in match if d.isdigit())} carat diamond')
else:
    print('Better luck next time')
