def get_lines_from_grid(grid: list[str], x: int, y: int) -> list[str]:
    lines = []
    lines.append(grid[y][x:])
    lines.append(grid[y][x::-1])
    lines.append("".join([grid[i][x] for i in range(y, len(grid))]))
    lines.append("".join([grid[i][x] for i in range(y, -1, -1)]))
    lines.append("".join([grid[y+i][x+i] for i in range(min(len(grid)-y, len(grid)-x))]))
    lines.append("".join([grid[y-i][x-i] for i in range(min(y+1, x+1))]))
    lines.append("".join([grid[y+i][x-i] for i in range(min(len(grid)-y, x+1))]))
    lines.append("".join([grid[y-i][x+i] for i in range(min(y+1, len(grid)-x))]))
    return lines


def look_for_xmas(grid: list[str], x: int, y: int) -> int:
    num_of_xmas = 0
    lines = get_lines_from_grid(grid, x, y)
    for line in lines:
        if line.startswith("XMAS"):
            num_of_xmas += 1
    return num_of_xmas


with open("input.txt", "r") as f:
    grid = f.readlines()

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "X":
            ans += look_for_xmas(grid, x, y)

print(ans)
