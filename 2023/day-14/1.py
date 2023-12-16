with open("input.txt") as f:
    platform = [line.strip() for line in f.readlines()]

platform_tr = ["".join(row) for row in zip(*platform)]

for i, col in enumerate(platform_tr):
    platform_tr[i] = "#".join(
        [
            "".join(sorted(portion, key=lambda x: 0 if x == "O" else 1))
            for portion in col.split("#")
        ]
    )

platform = ["".join(col) for col in zip(*platform_tr)]

load = 0
for i in range(len(platform)):
    for j in range(len(platform[0])):
        if platform[i][j] == "O":
            load += len(platform) - i

print(load)
