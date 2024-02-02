def step(map):
    reachable_points = []
    for i, row in enumerate(map):
        for j, pos in enumerate(row):
            if pos == "O":
                reachable_points.extend(
                    [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                )
                map[i][j] = "."
    for i, j in reachable_points:
        if i >= 0 and j >= 0 and i < len(map) and j < len(map[0]):
            if map[i][j] == ".":
                map[i][j] = "O"
    return map


with open("input.txt") as f:
    map = [list(s.strip().replace("S", "O")) for s in f.readlines()]

for _ in range(64):
    map = step(map)

res = 0
for row in map:
    for pos in row:
        res += pos == "O"

print(res)
