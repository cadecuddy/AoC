lines = [line.rstrip() for line in open('input.txt')]

def part_one():
    strengths = set([20, 60, 100, 140, 180, 220])
    x = 1
    ans = 0
    cycle = 0
    for line in lines:
        command = line.split(' ')[0]
        for _ in range(1 if command == "noop" else 2):
            cycle += 1
            if cycle in strengths:
                ans += cycle * x
        if command == "addx":
            x += int(line.split(' ')[1])
    return ans

def part_two():
    cycle = 0
    sprite = 1
    crt = []
    currentrow = ""
    for line in lines:
        command = line.split(' ')[0]
        for _ in range(1 if command == 'noop' else 2):
            cycle += 1
            if len(currentrow) in range(sprite - 1, sprite + 2):
                currentrow += "#"
            else:
                currentrow += " "
            if len(currentrow) == 40:
                crt.append(currentrow)
                currentrow = ""
        if command == 'addx':
            sprite += int(line.split(' ')[1])

    for x in crt:
        for y in x:
            print(y, end = '')
        print()

print(part_one())
part_two()
