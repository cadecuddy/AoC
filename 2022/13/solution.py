import functools

def cmp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return -1 if l < r else 1 if l > r else 0
    elif isinstance(l, int) and isinstance(r, list):
        return cmp([l], r)
    elif isinstance(l, list) and isinstance(r, int):
        return cmp(l, [r])
    else:
        for i in range(min(len(l), len(r))):
            c = cmp(l[i], r[i])
            if c != 0:
                return c
        return -1 if len(l) < len(r) else 1 if len(l) > len(r) else 0

packets = [[2], [6]]
lines = [list(map(eval,line.splitlines())) for line in open('input.txt').read().split("\n\n")]

def part_one():
    wrongidx = 0
    for i, line in enumerate(lines):
        l,r = line
        packets.append(l)
        packets.append(r)
        if cmp(l,r) == -1:
            wrongidx += i + 1
    return wrongidx

def part_two():
    # found functools via https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
    packets.sort(key=functools.cmp_to_key(cmp))
    return (packets.index([2]) + 1) * (packets.index([6]) + 1)

print(part_one())
print(part_two())