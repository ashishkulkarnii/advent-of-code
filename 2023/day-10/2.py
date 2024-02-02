from pprint import pprint

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

if j > 0 and j < len(diagram[i]) - 1 and diagram[i][j-1] == "-" and diagram[i][j+1] == "-":
    diagram[i] = diagram[i].replace("S", "-")
elif i > 0 and i < len(diagram) - 1 and diagram[i-1][j] == "|" and diagram[i+1][j] == "|":
    diagram[i] = diagram[i].replace("S", "|")
elif i > 0 and j > 0 and diagram[i-1][j] == "|" and diagram[i][j-1] == "-":
    diagram[i] = diagram[i].replace("S", "J")
elif i > 0 and j < len(diagram[i]) - 1 and diagram[i-1][j] == "|" and diagram[i][j+1] == "-":
    diagram[i] = diagram[i].replace("S", "L")
elif i < len(diagram) - 1 and j > 0 and diagram[i+1][j] == "|" and diagram[i][j-1] == "-":
    diagram[i] = diagram[i].replace("S", "7")
elif i < len(diagram) - 1 and j < len(diagram[i]) - 1 and diagram[i+1][j] == "|" and diagram[i][j+1] == "-":
    diagram[i] = diagram[i].replace("S", "F")


def direct(curr, direction):
    match diagram[curr[0]][curr[1]]:
        case "-":
            mark_visited(curr, "h")
            pass
        case "J":
            if direction == 0:
                mark_visited(curr, "^")
                direction = 90
            elif direction == 270:
                mark_visited(curr, "v")
                direction = 180
        case "7":
            if direction == 0:
                mark_visited(curr, "v")
                direction = 270
            elif direction == 90:
                mark_visited(curr, "^")
                direction = 180
        case "|":
            if direction == 90:
                mark_visited(curr, "^")
            elif direction == 270:
                mark_visited(curr, "v")
            pass
        case "L":
            if direction == 180:
                mark_visited(curr, "^")
                direction = 90
            elif direction == 270:
                mark_visited(curr, "v")
                direction = 0
        case "F":
            if direction == 90:
                mark_visited(curr, "^")
                direction = 0
            elif direction == 180:
                mark_visited(curr, "v")
                direction = 270
    return direction


def mark_visited(curr, char):
    diagram[curr[0]] = diagram[curr[0]][:curr[1]] + char + diagram[curr[0]][curr[1]+1:]


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

pprint(diagram)

move(curr, direction)
direction = direct(curr, direction)
while curr != start:
    curr = move(curr, direction)
    direction = direct(curr, direction)

for i in range(len(diagram)):
    for j in range(len(diagram[0])):
        if diagram[i][j] not in "v^hS":
            diagram[i] = diagram[i][:j] + "." + diagram[i][j+1:]

pprint(diagram)
inside = 0
for i in range(len(diagram)):
    # while "hh" in diagram[i]:
    #     diagram[i] = diagram[i].replace("hh", "h")
    # diagram[i] = diagram[i].replace("vhv", "v")
    # diagram[i] = diagram[i].replace("^h^", "^")
    # diagram[i] = diagram[i].replace("vh^", "h")
    # diagram[i] = diagram[i].replace("^hv", "h")
    for j in range(len(diagram[i])):
        if diagram[i][j] == "." and abs(diagram[i][:j].count("v") - diagram[i][:j].count("^")) % 2 == 1:
            inside += 1
            diagram[i] = diagram[i][:j] + "I" + diagram[i][j+1:]

pprint(diagram)
print(inside)