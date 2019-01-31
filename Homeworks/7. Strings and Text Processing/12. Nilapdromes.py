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
            core = re.sub(r'^'+max_nilaprome+'', '', line)
            core = re.sub(r'' + max_nilaprome + '$', '', core)
            print(core+max_nilaprome+core)
            break
        else:
            max_nilaprome = max_nilaprome[:-1]
