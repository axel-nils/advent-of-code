neighbors = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def parse_input(file):
    diagram = []
    with open(file) as f:
        for line in f:
            row = "l" + line.strip() + "r"
            diagram.append(row)
    width = len(diagram[0])
    diagram.insert(0, "t" * width)
    diagram.append("b" * width)
    for i, row in enumerate(diagram):
        diagram[i] = list(row)

    return diagram


def find_accessible(diagram):
    height = len(diagram)
    width = len(diagram[0])
    accessible = []
    for i in range(1, height):
        for j in range(1, width):
            if diagram[i][j] == "@":
                blocking = [diagram[i + y][j + x] == "@" for y, x in neighbors]
                if sum(blocking) < 4:
                    accessible.append((i, j))

    return accessible


def solve_part_one(file):
    diagram = parse_input(file)
    accessible = find_accessible(diagram)
    for y, x in accessible:
        diagram[y][x] = "x"

    print(f"Total removed: {len(accessible)}")


def solve_part_two(file):
    diagram = parse_input(file)
    accessible = True
    removed = 0
    while accessible:
        accessible = find_accessible(diagram)
        for y, x in accessible:
            diagram[y][x] = "x"
            removed += 1
        # print(len(accessible))

    print(f"Total removed: {removed}")


if __name__ == "__main__":
    solve_part_one("day4.txt")
    solve_part_two("day4.txt")
