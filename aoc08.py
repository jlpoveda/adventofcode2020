with open("./aoc08.txt") as file:
    lines = list(file.read().splitlines())

i = 0
visited_lines = []
accumulator = 0

while i < len(lines):
    if i in visited_lines:
        break
    instruction, value = lines[i].split(" ")
    visited_lines.append(i)
    if instruction == "nop":
        i += 1
    elif instruction == "acc":
        accumulator += int(value)
        i += 1
    elif instruction == "jmp":
        i += int(value)

print(f'Answer part 1: {accumulator}')

i = 0
visited_lines = []
accumulator = 0
changed_lines = {}


def reformat_lines(loops):
    finds = 0
    new_lines = lines.copy()
    for i, line in enumerate(new_lines):
        instruction, value = line.split(" ")
        if instruction == 'nop' or instruction == 'jmp':
            if instruction == 'nop' and int(value) == 0:
                continue
            if finds == loops:
                if instruction == 'nop':
                    new_lines[i] = f"jmp {value}"
                else:
                    new_lines[i] = f"nop {value}"
                return new_lines
            else:
                finds += 1


loops = 0
new_lines = lines.copy()
while i < len(lines):
    if i in visited_lines:
        visited_lines = []
        i = 0
        new_lines = reformat_lines(loops)
        loops += 1
        accumulator = 0

    try:
        instruction, value = new_lines[i].split(" ")
    except TypeError:
        print("==================")
        print(visited_lines)
        print(i)
        print(lines)
        exit()

    visited_lines.append(i)
    if instruction == "nop":
        i += 1
    elif instruction == "acc":
        accumulator += int(value)
        i += 1
    elif instruction == "jmp":
        i += int(value)


if i == len(lines):
    print(f'Answer part 2: {accumulator}')
