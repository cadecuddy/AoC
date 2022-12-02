from aocd import submit
day, year = 1, 2022

raw = open('input.txt').read()


def part_one():
    return max([sum([int(x) for x in y.split()]) for y in raw.split('\n\n')])

def part_two():
    return sum(sorted([sum([int(x) for x in y.split()]) for y in raw.split('\n\n')])[-3:])

print(part_one())
print(part_two())
