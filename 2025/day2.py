import re

twice_pattern = re.compile(r"^(\d+)\1$")

at_least_twice_pattern = re.compile(r"^(\d+)\1+$")


def is_repeated_twice(n):
    return bool(twice_pattern.fullmatch(str(n)))


def is_repeated_at_least_twice(n):
    return bool(at_least_twice_pattern.fullmatch(str(n)))


def solve_part_one(file):
    with open(file) as f:
        full_list = f.readline()

    sum_of_invalid = 0
    for line in full_list.strip().split(","):
        first, last = map(int, line.split("-"))
        for n in range(first, last + 1):
            if is_repeated_twice(n):
                sum_of_invalid += n
    print(f"Total sum: {sum_of_invalid}")


def solve_part_two(file):
    with open(file) as f:
        full_list = f.readline()

    sum_of_invalid = 0
    for line in full_list.strip().split(","):
        first, last = map(int, line.split("-"))
        for n in range(first, last + 1):
            if is_repeated_at_least_twice(n):
                sum_of_invalid += n
    print(f"Total sum: {sum_of_invalid}")


if __name__ == "__main__":
    solve_part_one("day2.txt")
    solve_part_two("day2.txt")
