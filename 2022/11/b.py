from collections import defaultdict
import re

m = defaultdict(list)
monkeys = [[x.split("\n") for x in line.split('\n\n')] for line in open('input.txt').read().split('\n\n')]
operations = []
values = []
tests = []
testTrues = []
testFalses = [] 
inspects = defaultdict(int)
n = 1
for x in range(len(monkeys)): inspects[x] = 0

# setup
for i, monkey in enumerate(monkeys):
    numbers = re.findall(r'\d+', monkey[0][1])
    m[i] = [int(x) for x in numbers]
    _, operation, val = monkey[0][2].split(" = ")[1].split(" ")

    operations.append(operation)
    values.append(int(val)) if val.isnumeric() else values.append("old")

    test = monkey[0][3].split(": ")[1].split(" ")[2]
    tests.append(int(test))

    testTrue = monkey[0][4].split(": ")[1].split(" ")[3]
    testTrues.append(int(testTrue))
    n *= int(test)
    testFalse = monkey[0][5].split(": ")[1].split(" ")[3]
    testFalses.append(int(testFalse))

def part_two():
    for _ in range(10000):
        for i in range(len(monkeys)):
            for itemworry in m[i]:
                og = itemworry
                inspects[i] += 1
                if operations[i] == "*":
                    if values[i] == "old":
                        og = og * og
                    else:
                        og = og * values[i]
                else:
                    og = og + values[i]
                og %= n
                m[testTrues[i]].append(og) if og % tests[i] == 0 else m[testFalses[i]].append(og)
            m[i] = []

    return sorted(inspects.values(), reverse=True)[0] * sorted(inspects.values(), reverse=True)[1]

print(part_two())