import math
import re

while True:
    line = input()
    if line == 'end':
        break

    half = math.floor((len(line)/2))
    if len(line)%2 == 0:
        half -= 1
    max_nilaprome = line[:half]
    search_nilaprome = line[half:]

    while len(max_nilaprome)>0:
        if max_nilaprome == line[-len(max_nilaprome):]:
            line = re.sub(r'^'+max_nilaprome+'', '', line)
            line = re.sub(r'' + max_nilaprome + '$', '', line)
            print(line+max_nilaprome+line)
            break
        else:
            max_nilaprome = max_nilaprome[:-1]
