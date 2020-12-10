from itertools import combinations

with open("./aoc09.txt") as file:
    input = list(map(lambda x: int(x), file.read().splitlines()))


def search_weakness(value, input):
    for size in range(2, 100):
        j = size
        while j < len(input):
            if sum(input[j-size:j]) == value:
                print(input[j-size:j])
                print("Result for 2:", max(input[j-size:j]) + min(input[j-size:j]), max(input[j-size:j]), min(input[j-size:j]))
                return True
            j += 1


preamble = 25
j = preamble
while j < len(input):
    found = False
    for i in list(combinations(input[j-preamble:j], 2)):
        if sum(i) == input[j]:
            found = True
            break
    if not found:
        print(f"Result for problem 1: {input[j]}")
        break
    j += 1

search_weakness(input[j], input)


