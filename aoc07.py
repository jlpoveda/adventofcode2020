from pathlib import Path
from collections import defaultdict, deque

# Reading input
filename = Path("aoc07.txt")
rules = {}

with open(filename, 'r') as file_:
    for line in file_:
        s = line.strip().split(' bags contain ')

        content = defaultdict(int)
        for comp in s[1].split(', '):
            words = comp.split(' ')
            if words[0] != 'no':
                content[words[1] + ' ' + words[2]] = int(words[0])
        rules[s[0]] = content

# Part 1
bags = set(['shiny gold'])
l = 0

# Continue to execute this function until no new items are added to the set bags
while len(bags) > l:
    l = len(bags)
    # Iterate over the rules, if the rule contains anything in the set bags, add the key for that rule to the set bags
    [bags.add(key) for key in rules if any(color in rules[key].keys() for color in bags)]

print(f'Answer part 1: {len(bags) - 1}')

# Part 2
bags2 = defaultdict(int)
q = deque([('shiny gold', 1)])

while len(q) > 0:
    color, amount = q.pop()

    for key in rules[color]:
        q.append((key, rules[color][key] * amount))
        bags2[key] += rules[color][key] * amount

print(f'Answer part 2: {sum(bags2.values())}')