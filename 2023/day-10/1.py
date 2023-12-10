with open("input.txt") as f:
    diagram = f.readlines()

start = None
for i, line in enumerate(diagram):
    diagram[i] = line.strip()
    if not start:
        for j, tile in enumerate(diagram[i]):
            if tile == "S":
                start, curr = [i, j], [i, j]
                break

i, j = start
if j < len(diagram[0]) and diagram[j][j+1] in "-7J":
    direction = 0
elif i > 0 and diagram[i-1][j] in "|7F":
    direction = 90
elif j > 0 and diagram[i][j-1] in "-FL":
    direction = 180
elif i < len(diagram) - 1 and diagram[i+1][j] in "|JL":
    direction = 270


def direct(curr, direction):
    match diagram[curr[0]][curr[1]]:
        case "-":
            pass
        case "J":
            if direction == 0:
                direction = 90
            elif direction == 270:
                direction = 180
        case "7":
            if direction == 0:
                direction = 270
            elif direction == 90:
                direction = 180
        case "|":
            pass
        case "L":
            if direction == 180:
                direction = 90
            elif direction == 270:
                direction = 0
        case "F":
            if direction == 90:
                direction = 0
            elif direction == 180:
                direction = 270
    return direction


def move(curr, direction):
    match direction:
        case 0:
            curr[1] += 1
        case 90:
            curr[0] -= 1
        case 180:
            curr[1] -= 1
        case 270:
            curr[0] += 1
    return curr


move(curr, direction)
direction = direct(curr, direction)
steps = 1
while curr != start:
    curr = move(curr, direction)
    direction = direct(curr, direction)
    steps += 1

print(steps // 2 + (steps % 2 > 0))
