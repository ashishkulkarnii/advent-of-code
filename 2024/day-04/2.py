with open("input.txt", "r") as f:
    grid = f.readlines()

ans = 0
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == "A":
            d1 = grid[y-1][x-1] + "A" + grid[y+1][x+1]
            d2 = grid[y-1][x+1] + "A" + grid[y+1][x-1]
            if (d1 == "MAS" or d1 == "SAM") and (d2 == "SAM" or d2 == "MAS"):
                ans += 1

print(ans)
