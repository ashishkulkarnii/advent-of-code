import copy


with open("input.txt") as f:
    platform = [line.strip() for line in f.readlines()]


def tilt(direction, platform):
    match direction:
        case "north":
            platform_tr = ["".join(row) for row in zip(*platform)]
            for i, col in enumerate(platform_tr):
                platform_tr[i] = "#".join(
                    [
                        "".join(sorted(portion, key=lambda x: 0 if x == "O" else 1))
                        for portion in col.split("#")
                    ]
                )
            platform = ["".join(col) for col in zip(*platform_tr)]
        case "east":
            for i, row in enumerate(platform):
                platform[i] = "#".join(
                    [
                        "".join(sorted(portion, key=lambda x: 1 if x == "O" else 0))
                        for portion in row.split("#")
                    ]
                )
        case "south":
            platform_tr = ["".join(row) for row in zip(*platform)]
            for i, col in enumerate(platform_tr):
                platform_tr[i] = "#".join(
                    [
                        "".join(sorted(portion, key=lambda x: 1 if x == "O" else 0))
                        for portion in col.split("#")
                    ]
                )
            platform = ["".join(col) for col in zip(*platform_tr)]
        case "west":
            for i, row in enumerate(platform):
                platform[i] = "#".join(
                    [
                        "".join(sorted(portion, key=lambda x: 0 if x == "O" else 1))
                        for portion in row.split("#")
                    ]
                )
    return platform


def cycle(platform):
    platform = tilt("north", platform)
    platform = tilt("west", platform)
    platform = tilt("south", platform)
    platform = tilt("east", platform)
    return platform


load_history = []

for _ in range(1000000000):
    prev = copy.deepcopy(platform)
    platform = cycle(platform)

    load = 0
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == "O":
                load += len(platform) - i
    load_history.append(load)
    print(load)

print(load_history[-1])
