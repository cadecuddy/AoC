lines = [[int(x) for x in line.rstrip()] for line in open("input.txt")]

def part_one():
    # start w perimeter
    visible = (len(lines) * 2) + (len(lines[0]) * 2 ) - 4
    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            current = lines[r][c]
            
            left = lines[r][:c]
            right = lines[r][c + 1:]
            top = [lines[i][c] for i in range(0, r)]
            bottom = [lines[i][c] for i in range(r + 1, len(lines))]

            if max(left) < current or max(right) < current or max(top) < current or max(bottom) < current:
                visible += 1
    return visible

def part_two():
    scenic = 0
    # edges don't count since they're guarunteed at least a 0
    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            current = lines[r][c]
            # count left
            left = 0
            for i in range(c, -1, -1):
                if i == c: continue
                if lines[r][i] < current:
                    left += 1
                else:
                    left += 1
                    break
            # count right
            right = 0
            for i in range(c, len(lines[0])):
                if i == c: continue
                if i > len(lines[0]): break
                if lines[r][i] < current:
                    right += 1
                else:
                    right += 1
                    break
            # count top
            top = 0
            for i in range(r, -1, -1):
                if i == r: continue
                if i < 0: break
                if lines[i][c] < current:
                    top += 1
                else:
                    top += 1
                    break
            # count bottom
            bottom = 0
            for i in range(r + 1, len(lines)):
                if i == r: continue
                if lines[i][c] < current:
                    bottom += 1
                else:
                    bottom += 1
                    break
            scenic = max(scenic, right * left * top * bottom)
    return scenic

print(part_one())
print(part_two())