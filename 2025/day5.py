def parse_input(file):
    fresh = []
    available = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line != "":
                if "-" in line:
                    fresh.append([int(d) for d in line.split("-")])
                else:
                    available.append(int(line))

    return sorted(fresh), available


def merge_ranges(sorted_ranges):
    merged = []
    for i, (low, high) in enumerate(sorted_ranges):
        if i == 0:
            merged.append([low, high])
        previous_high = merged[-1][1]
        if low > previous_high:
            merged.append([low, high])
        else:
            merged[-1][1] = max(high, previous_high)
    return merged


def is_fresh(fresh, id):
    if id < fresh[0][0] or id > fresh[-1][1]:
        return False
    for low, high in fresh:
        if id < low:
            return False
        if id <= high:
            return True
    raise AssertionError


def solve_part_one(file):
    fresh, available = parse_input(file)
    fresh = merge_ranges(fresh)
    fresh_ingredients = sum([is_fresh(fresh, id) for id in available])

    print(f"Fresh ingredient IDs: {fresh_ingredients}")


def solve_part_two(file):
    fresh, _ = parse_input(file)
    fresh = merge_ranges(fresh)
    id_sum = sum([high - low + 1 for low, high in fresh])

    print(f"Total fresh ingredient IDs: {id_sum}")


if __name__ == "__main__":
    solve_part_one("day5.txt")
    solve_part_two("day5.txt")
