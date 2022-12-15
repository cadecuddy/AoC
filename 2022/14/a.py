block = set()
cutoff = 0 # max y value in rocks

# find all blocked coords
for line in open("input.txt"):
    coords = [list(map(int, eval(pair))) for pair in line.strip().split(" -> ")]
    # cool packing trick from hyper-neutrino's 
    # video on this question https://www.youtube.com/watch?v=Uf_IF_3RbKw
    for (x1, y1), (x2, y2) in list(zip(coords, coords[1:])):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                block.add((x,y))
                cutoff = max(cutoff, y)

# down, left, right
t = 0
while True:
    (x,y) = (500, 0)
    while True:
        if y == cutoff:
            print(t)
            exit()
        if (x, y + 1) not in block:
            y += 1
        elif (x - 1, y + 1) not in block:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in block:
            x += 1
            y += 1
        else:
            break
    t += 1
    block.add((x,y))