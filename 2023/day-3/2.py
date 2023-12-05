import re
import collections
import math

gears = collections.defaultdict(list)

with open("input.txt") as f:
    lines = f.readlines()

for row, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for m in matches:
        start, end, n = m.start(0), m.end(0), m.group(0)
        num_res = 0
        neighbours = ""
        if row > 0:
            above = lines[row-1][max(0, start - 1):min(end + 1, len(line))]
            for i, c in enumerate(above):
                if c == "*":
                    gears[(row - 1, max(0, start - 1) + i)].append(int(n))
        if row < len(lines) - 1:
            below = lines[row+1][max(0, start - 1):min(end + 1, len(line))]
            for i, c in enumerate(below):
                if c == "*":
                    gears[(row + 1, max(0, start - 1) + i)].append(int(n))
        if start > 0 and line[start-1] == "*":
            gears[(row, start - 1)].append(int(n))
        if end < len(line) and line[end] == "*":
            gears[(row, end)].append(int(n))

res = 0

for _, nums in gears.items():
    if len(nums) == 2:
        res += math.prod(nums)

print(res)
