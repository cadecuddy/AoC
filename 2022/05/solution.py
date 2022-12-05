lines = [line.rstrip() for line in open("input.txt")]

def parse_stacks():
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in lines[0:8]:
        for x in range(1, len(line), 4):
            if line[x] != " ":
                stacks[x // 4].insert(0, line[x])
    return stacks

def part_one():
    t = ""
    stacks = parse_stacks()
    for line in lines[10:]:
        command = line.split(" ")
        for x in range(int(command[1])):
            item = stacks[int(command[3]) - 1].pop()
            stacks[int(command[5]) - 1].append(item)
    for stack in stacks:
        t += stack.pop()
    return t


def part_two():
    t = ""
    stacks = parse_stacks()
    for line in lines[10:]:
        command = line.split(" ")
        new = []
        for x in range(int(command[1])):
            item = stacks[int(command[3]) - 1].pop()
            new.append(item)
        new.reverse()
        stacks[int(command[5]) - 1].extend(new)
    for stack in stacks:
        t += stack.pop()
    return t

print(part_one())
print(part_two())