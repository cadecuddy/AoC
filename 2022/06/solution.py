line = open("input.txt").read().rstrip()

def part_one():
    for i in range(len(line)):
        if len(set(line[i:i+4])) == 4:
            return i + 4

def part_two():
    for i in range(len(line)):
        if len(set(line[i:i+14])) == 14:
            return i + 14

print(part_one())
print(part_two())