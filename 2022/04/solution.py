d = [line.rstrip() for line in open("input.txt")]

def part_one():
    t = 0
    for l in d:
        s = l.split(",")
        p1, p2 = [int(x) for x in s[0].split("-")], [int(x) for x in s[1].split("-")]
        # p2 is entirely inside of p1 or vice versa
        if (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1]):
            t += 1
    return t

def part_two():
    t = 0
    for l in d:
        s = l.split(",")
        p1, p2 = [int(x) for x in s[0].split("-")], [int(x) for x in s[1].split("-")]
        # if they're not NOT overlapping :)
        if not (p1[1] < p2[0] or p2[1] < p1[0]):
            t += 1
    return t

print(part_one())
print(part_two())