with open("input.txt") as f:
    space = list(map(lambda x: x.strip(), f.readlines()))

# adding space vertically
for i, row in enumerate(space):
    if row.count(".") == len(row):
        space[i] = row.replace(".", "-")

# adding space horizontally
for col in range(len(space[0])):
    all_dot = True
    for row in range(len(space)):
        if space[row][col] == "#":
            all_dot = False
    if all_dot:
        for row in range(len(space)):
            space[row] = space[row][:col] + ("|" if space[row][col] == "." else "+") + space[row][col+1:]

# locating galaxies
galaxies = []
for row in range(len(space)):
    for col in range(len(space[0])):
        if space[row][col] == "#":
            galaxies.append((row, col))

res = 0

for i, galaxy1 in enumerate(galaxies[:-1]):
    for j, galaxy2 in list(enumerate(galaxies))[i+1:]:
        y1, y2 = galaxy1[0], galaxy2[0]
        x1, x2 = galaxy1[1], galaxy2[1]

        step = 1 if y1 < y2 else -1
        for y in range(y1, y2, step):
            if space[y][x1] in "-+":
                res += 1000000
            else:
                res += 1

        step = 1 if x1 < x2 else -1
        for x in range(x1, x2, step):
            if space[y2][x] in "|+":
                res += 1000000
            else:
                res += 1

print(res)
