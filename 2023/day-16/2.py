with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]


def next(i, j, dir, grid, verbose=False):
    if not (i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0):
        return
    is_energized[i][j] = True

    if verbose:
        for row in is_energized:
            for tile in row:
                if tile:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(i, j, dir)
        print()

    match dir:
        case "right":
            match grid[i][j]:
                case "-" | ".":
                    return [(i, j + 1, dir)]
                case "|":
                    return [(i - 1, j, "up"), (i + 1, j, "down")]
                case "/":
                    return [(i - 1, j, "up")]
                case "\\":
                    return [(i + 1, j, "down")]
        case "left":
            match grid[i][j]:
                case "-" | ".":
                    return [(i, j - 1, dir)]
                case "|":
                    return [(i - 1, j, "up"), (i + 1, j, "down")]
                case "/":
                    return [(i + 1, j, "down")]
                case "\\":
                    return [(i - 1, j, "up")]
        case "up":
            match grid[i][j]:
                case "|" | ".":
                    return [(i - 1, j, dir)]
                case "-":
                    return [(i, j - 1, "left"), (i, j + 1, "right")]
                case "/":
                    return [(i, j + 1, "right")]
                case "\\":
                    return [(i, j - 1, "left")]
        case "down":
            match grid[i][j]:
                case "|" | ".":
                    return [(i + 1, j, dir)]
                case "-":
                    return [(i, j - 1, "left"), (i, j + 1, "right")]
                case "/":
                    return [(i, j - 1, "left")]
                case "\\":
                    return [(i, j + 1, "right")]

max_res = 0

for i in range(len(grid)):
    is_energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = [(i, 0, "right")]
    visited = set()

    while queue:
        i, j, dir = queue.pop(0)
        if (i, j, dir) not in visited:
            if x := next(i, j, dir, grid):
                queue.extend(x)
            visited.add((i, j, dir))

    res = 0
    for row in is_energized:
        for tile in row:
            if tile:
                res += 1
    max_res = max(max_res, res)

for i in range(len(grid)):
    is_energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = [(i, len(grid[0]) - 1, "left")]
    visited = set()

    while queue:
        i, j, dir = queue.pop(0)
        if (i, j, dir) not in visited:
            if x := next(i, j, dir, grid):
                queue.extend(x)
            visited.add((i, j, dir))

    res = 0
    for row in is_energized:
        for tile in row:
            if tile:
                res += 1
    max_res = max(max_res, res)

for i in range(len(grid[0])):
    is_energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = [(0, i, "down")]
    visited = set()

    while queue:
        i, j, dir = queue.pop(0)
        if (i, j, dir) not in visited:
            if x := next(i, j, dir, grid):
                queue.extend(x)
            visited.add((i, j, dir))

    res = 0
    for row in is_energized:
        for tile in row:
            if tile:
                res += 1
    max_res = max(max_res, res)

for i in range(len(grid[0])):
    is_energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = [(len(grid) - 1, i, "up")]
    visited = set()

    while queue:
        i, j, dir = queue.pop(0)
        if (i, j, dir) not in visited:
            if x := next(i, j, dir, grid):
                queue.extend(x)
            visited.add((i, j, dir))

    res = 0
    for row in is_energized:
        for tile in row:
            if tile:
                res += 1
    max_res = max(max_res, res)


print(max_res)
