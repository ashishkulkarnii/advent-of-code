import re

res = 0

with open("input.txt") as f:
    lines = f.readlines()

for row, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for m in matches:
        start, end, n = m.start(0), m.end(0), m.group(0)
        num_res = 0
        neighbours = ""
        if row > 0:
            neighbours += lines[row-1][max(0, start - 1):min(end + 1, len(line))]
        if row < len(lines) - 1:
            neighbours += lines[row+1][max(0, start - 1):min(end + 1, len(line))]
        if start > 0:
            neighbours += line[start-1]
        if end < len(line):
            neighbours += line[end]
        symbol = neighbours.replace("\n", "").replace(".", "")
        if symbol:
            res += int(n)

print(res)
