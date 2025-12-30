from functools import reduce


def solve_problem(problem):
    numbers, operator = problem[:-1], problem[-1]
    match operator:
        case "+":
            return reduce(lambda x, y: int(x) + int(y), numbers)
        case "*":
            return reduce(lambda x, y: int(x) * int(y), numbers)


def solve_part_one(file):
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.strip().split())
    grand_total = sum([solve_problem(p) for p in zip(*lines)])
    print(f"Grand total: {grand_total}")


def solve_part_two(file):
    problems = []
    with open(file) as f:
        lines = f.readlines()
    for p in zip(*lines):
        op = p[-1].strip()
        if op:
            problems.append([op])
        nums = "".join(p[:-1]).strip()
        if nums:
            last_problem = problems[-1]
            problems[-1] = [nums, *last_problem]

    grand_total = sum([solve_problem(p) for p in problems])

    print(f"Grand total: {grand_total}")


if __name__ == "__main__":
    solve_part_one("day6.txt")
    solve_part_two("day6.txt")
