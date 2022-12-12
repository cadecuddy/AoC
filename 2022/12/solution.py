from collections import deque
lines = [[x for x in line.rstrip()] for line in open("input.txt")]

start, end = None, None
starts = []
for r, row in enumerate(lines):
    for c, col in enumerate(row):
        if col == "S":
            start = (r, c)
            starts.append((r, c))
            lines[r][c] = "a"
        elif col == "E":
            end = (r, c)
            lines[r][c] = "z"
        elif lines[r][c] == "a":
            starts.append((r, c))

def bfs(start, end, mode):
    queue = deque([(start, 0) for start in starts] if mode == 2 else [(start, 0)])
    visited = set()
    while queue:
        (r, c), steps = queue.popleft()
        if (r, c) == end:
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(lines) and 0 <= nc < len(lines[nr]) and ord(lines[nr][nc]) - ord(lines[r][c]) <= 1:
                queue.append(((nr, nc), steps + 1))

def part_one():
    return bfs(start, end, 1)

def part_two():
    return bfs(start, end, 2)

print(part_one())
print(part_two())