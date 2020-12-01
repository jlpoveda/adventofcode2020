with open("./aoc01.txt") as file:
    input = list(map(lambda x: int(x), file.read().splitlines()))

"""
This was my first approach and it worked

for x in input:
    for y in input:
        for z in input:
            if x + y + z == 2020:
                print(x * y * z)
                exit()
                
But later I found a more pythonic way to solve de problem
"""
from itertools import combinations

for i in list(combinations(input, 2)):
    if sum(i) == 2020:
        print(i[0] * i[1])

for i in list(combinations(input, 3)):
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])
