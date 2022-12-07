import os.path
from collections import defaultdict

lines = [line.rstrip() for line in open("input.txt")]

d = defaultdict(int)
def part_one():
    c = "/"
    for line in lines:
        s = line.split(" ")
        if s[0] == "$":
            command = s[1]
            if command == "cd":
                if s[2] == "..":
                    c = os.path.dirname(c)
                else:
                    c = os.path.join(c, s[2])
        elif s[0].isnumeric():
            # add file size to directory
            d[c] += int(s[0])
            # update parent directory sizes
            temp = c
            while os.path.dirname(temp) != temp:
                temp = os.path.dirname(temp)
                d[temp] += int(s[0])
                
    t = sum (v for v in d.values() if v <= 100000)
    return t

def part_two():
    # get how much we need to delete
    space_needed = 30000000 - (70000000 - d["/"])
    return min(size for size in d.values() if size >= space_needed)

print(part_one())
print(part_two())