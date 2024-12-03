import re


with open("input.txt", "r") as f:
    mem = f.read()

pos = 0
matches = []
pattern = re.compile(r"mul\(\d+,\d+\)")
while m := pattern.search(mem, pos):
    pos = m.start() + 1
    matches.append(m[0])

res = 0
for match in matches:
    n1, n2 = match.split(",")
    res += int(n1[4:]) * int(n2[:-1])

print(res)
