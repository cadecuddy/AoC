lines = [line.rstrip() for line in open("input.txt")]
total = 0

# Yucky hardcoding

def part_one():
    outcome = {"A X": 3 + 1, "A Y": 6 + 2, "A Z": 0 + 3, 
            "B X": 0 + 1, "B Y": 3 + 2, "B Z": 6 + 3, 
            "C X": 6 + 1, "C Y": 0 + 2, "C Z": 3 + 3,}
    total = 0
    for line in lines:
        total += outcome[line]
    return total

def part_two():
    move = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    beats = {"A": "Y", "B": "Z", "C": "X"}
    lose = {"A": "Z", "B": "X", "C": "Y"}
    total2 = 0
    for line in lines:
        opp, outcome = line.split()
        # lose
        if outcome == "X":
            total2 += move[lose[opp]]
        # draw
        elif outcome == "Y":
            total2 += 3
            total2 += move[opp]
        # win
        elif outcome == "Z":
            total2 += 6
            total2 += move[beats[opp]]
    return total2

        
print(part_one())
print(part_two())