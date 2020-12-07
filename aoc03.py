with open("./aoc03.txt") as file:
    input = list(file.read().splitlines())

complete = []
len_complete = len(complete)
for i, line in enumerate(input):
    complete.append("")
    for _ in range(300):
        complete[i] += line

trees = []

movements = [1, 3, 5, 7]
for movement in movements:
    total_trees = 0
    for n, line in enumerate(complete):
        if n > 0 and line[n*movement] == '#':
            total_trees += 1
    trees.append(total_trees)

total_trees = 0
i = 0
for n in range(0, len(complete), 2):
    if complete[n][i] == '#':
        total_trees += 1
    i += 1

trees.append(total_trees)

result = 1
for t in trees:
    result *= t

print(result)
