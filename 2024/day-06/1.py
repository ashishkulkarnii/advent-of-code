def change_direction(direction: int) -> int:
    return (direction - 90) % 360


def get_direction(guard: str) -> int:
    guard_direction = {
        ">": 0,
        "^": 90,
        "<": 180,
        "v": 270,
    }
    return guard_direction.get(guard, -1)


def move_in_direction(pos: list[int], direction: int) -> list[int]:
    x, y = pos
    match direction:
        case 0:
            return [x + 1, y]
        case 90:
            return [x, y - 1]
        case 180:
            return [x - 1, y]
        case 270:
            return [x, y + 1]
        case _:
            raise ValueError("Invalid direction")


def find_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] not in [".", "#", "*"]:
                pos = [x, y]
                direction = get_direction(grid[y][x])
                return pos, direction


with open("input.txt", "r") as f:
    grid = f.read().split("\n")

# pad grid with *s
grid = [f"*{row}*" for row in grid]
grid = [len(grid[0]) * "*"] + grid + [len(grid[0]) * "*"]
grid = [list(row) for row in grid]

pos, direction = find_guard(grid)
while grid[pos[1]][pos[0]] != "*":
    x, y = move_in_direction(pos, direction)
    if grid[y][x] != "#":
        grid[pos[1]][pos[0]] = "X"
        pos = [x, y]
    else:
        direction = change_direction(direction)

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        ans += grid[y][x] == "X"
print(ans)
