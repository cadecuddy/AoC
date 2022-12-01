from aocd import submit
day, year = 1, 2022

raw = open('input.txt').read()


def part_one():
    return max([sum([int(x) for x in y.split()]) for y in raw.split('\n\n')])

def part_two():
    return sum(sorted([sum([int(x) for x in y.split()]) for y in raw.split('\n\n')])[-3:])

submit(part_one(), part="a", day=day, year=year)
submit(part_two(), part="b", day=day, year=year)