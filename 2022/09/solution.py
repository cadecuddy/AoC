lines = [line.rstrip() for line in open('input.txt')]

def part_one():
    visited = set((0,0))
    headpos = [0, 0]
    tailpos = [0, 0]
    for line in lines:
        dir, steps = line.split(" ")
        steps = int(steps)

        for _ in range(steps):
            if dir == "R":
                headpos[0] += 1
            elif dir == "L":
                headpos[0] -= 1
            elif dir == "U":
                headpos[1] += 1
            elif dir == "D":
                headpos[1] -= 1
            while max(abs(tailpos[0] - headpos[0]), abs(tailpos[1] - headpos[1])) > 1:
                if abs(tailpos[0] - headpos[0]) > 0:
                    tailpos[0] += 1 if tailpos[0] < headpos[0] else -1
                if abs(tailpos[1] - headpos[1]) > 0:
                    tailpos[1] += 1 if tailpos[1] < headpos[1] else -1
                visited.add(tuple(tailpos))
    return len(visited)

def part_two():
    visited = set()
    ropes = [[0, 0]] * 10
    for line in lines:
        dir, steps = line.split(" ")
        steps = int(steps)
        for _ in range(steps):
            # update the head
            head = ropes[0]
            if dir == "R":
                head[0] += 1
            elif dir == "L":
                head[0] -= 1
            elif dir == "U":
                head[1] += 1
            elif dir == "D":
                head[1] -= 1
            ropes[0] = head
            # update the 9 other ropes
            for i in range(1, len(ropes)):
                lastrope = ropes[i - 1]
                currentrope = ropes[i].copy()
                while max(abs(currentrope[0] - lastrope[0]), abs(currentrope[1] - lastrope[1])) > 1:
                    if abs(currentrope[0] - lastrope[0]) > 0:
                        currentrope[0] += 1 if currentrope[0] < lastrope[0] else -1
                    if abs(currentrope[1] - lastrope[1]) > 0:
                        currentrope[1] += 1 if currentrope[1] < lastrope[1] else -1
                ropes[i] = currentrope
            # add the tail to the set
            visited.add(tuple(ropes[-1]))
    return len(visited)

print(part_one())
print(part_two())