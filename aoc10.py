import collections

with open("./aoc10.txt") as file:
    input = list(map(lambda x: int(x), file.read().splitlines()))

input = sorted(input)

# part 1
hops = collections.defaultdict(lambda: 1)
for i in range(1, len(input)):
    hops[input[i] - input[i-1]] += 1

print(f"Answer to part 1: {hops[1] * hops[3]}")

# part 2
combinations = collections.defaultdict(int, {0: 1})
for adapter in input:
    combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]

print(f"Answer to part 2: {combinations[input[-1]]}")
