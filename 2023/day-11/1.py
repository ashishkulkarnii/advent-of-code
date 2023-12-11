with open("input.txt") as f:
    space = list(map(lambda x: x.strip(), f.readlines()))

# adding space vertically
i = 0
while i < len(space):
    if space[i].count(".") == len(space[i]):
        space.insert(i, space[i])
        i += 1
    i += 1

# adding space horizontally
for col in range(len(space[0])):
    all_dot = True
    for row in range(len(space)):
        if space[row][col] != ".":
            all_dot = False
    if all_dot:
        for row in range(len(space)):
            space[row] = space[row][:col] + "-" + space[row][col+1:]
for row in range(len(space)):
    space[row] = space[row].replace("-", "..")

# locating galaxies
galaxies = []
for row in range(len(space)):
    for col in range(len(space[0])):
        if space[row][col] == "#":
            galaxies.append((row, col))

res = 0

for i, galaxy1 in enumerate(galaxies[:-1]):
    for j, galaxy2 in enumerate(galaxies[i+1:]):
        dist = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
        res += dist

print(res)
