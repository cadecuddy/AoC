data = [line.rstrip() for line in open('input.txt')]

def part_one():
    total = 0
    for line in data:
        n = len(line) // 2
        one, two = line[:n], line[n:]
        c, = set(one) & set(two)
        total += ord(c) - 96 if c.islower() else ord(c) - 38
    return total

def part_two():
    total = 0
    for i in range(0, len(data), 3):
        one, two, three = data[i], data[i+1], data[i+2]
        c, = set(one) & set(two) & set(three)
        total += ord(c) - 96 if c.islower() else ord(c) - 38
    return total

print(part_one())
print(part_two())
