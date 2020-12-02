import re

with open("./aoc02.txt") as file:
    input = list(file.read().splitlines())

valids = 0
for password in input:
    match = re.match(r'(\d+)\-(\d+)\s(\w):\s(\w+)', password)
    x, y, letter, pwd = match[1], match[2], match[3], match[4]

    if int(x) <= pwd.count(letter) <= int(y):
        valids += 1
print(valids)

# Second part
valids = 0
for password in input:
    match = re.match(r'(\d+)\-(\d+)\s(\w):\s(\w+)', password)
    x, y, letter, pwd = match[1], match[2], match[3], match[4]

    if not (pwd[int(x) - 1] == letter and pwd[int(y) - 1] == letter) \
            and (pwd[int(x) - 1] == letter or pwd[int(y) - 1] == letter):
        valids += 1
print(valids)
