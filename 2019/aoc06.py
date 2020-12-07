"""
Day 6: Universal Orbit Map
"""

from treelib import Node, Tree
from treelib.exceptions import NodeIDAbsentError

with open("./aoc06.txt") as file:
    input = list(file.read().splitlines())

# root, first = input[0].split(')')

tree = Tree()
# tree.create_node(root, root)  # root node
# tree.create_node(first, first, parent=root)

for i in range(0, len(input)):
    parent, n = input[i].split(')')
    try:
        tree.create_node(n, n, parent=parent)
    except NodeIDAbsentError:
        tree.create_node(parent, parent)
        tree.create_node(n, n, parent=parent)

paths = tree.paths_to_leaves()

result = 0
planets = []
for path in paths:
    text = ''
    for i, planet in enumerate(path):
        text += planet
        if text not in planets:
            planets.append(text)
            result += i

print(result)
