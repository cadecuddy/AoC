from aocd import get_data, submit
d, y = 1, 2021


def part_one():
    data = get_data(day=d, year=y)
    ans = 1195

    return ans

def part_two():
    data = get_data(day=d, year=y)
    ans = 1235

    return ans

submit(part_one(), part="a", day=d, year=y)
submit(part_two(), part="b", day=d, year=y)