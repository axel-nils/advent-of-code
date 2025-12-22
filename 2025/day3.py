def solve_part_one(file):
    with open(file) as f:
        full_list = f.readlines()

    total_joltage = 0
    for line in full_list:
        s = line.strip()
        m = max(s)
        i = s.index(m)
        if i == len(s) - 1:  # max is last
            n = max(s[:i])
            print(n, m)
            total_joltage += int(n + m)
        else:
            n = max(s[i + 1 :])
            print(m, n)
            total_joltage += int(m + n)

    print(f"Total sum: {total_joltage}")


def max_number_with_order(s, n):
    stack = []
    remaining = len(s)

    for digit in s:
        can_pop = len(stack) > 0
        can_replace = stack and digit > stack[-1]
        enough_remaining = len(stack) - 1 + remaining >= n

        while can_replace and enough_remaining:
            stack.pop()
            can_replace = stack and digit > stack[-1]
            enough_remaining = len(stack) - 1 + remaining >= n

        if len(stack) < n:
            stack.append(digit)

        remaining -= 1

    return "".join(stack[:n])


def solve_part_two(file):
    with open(file) as f:
        full_list = f.readlines()

    total_joltage = 0
    for line in full_list:
        s = line.strip()
        max_joltage = max_number_with_order(s, 12)
        total_joltage += int(max_joltage)

    print(f"Total sum: {total_joltage}")


if __name__ == "__main__":
    solve_part_one("day3.txt")
    solve_part_two("day3.txt")
