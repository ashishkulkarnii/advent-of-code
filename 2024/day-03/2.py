import re


with open("input.txt", "r") as f:
    mem = f.read()

pos = 0
matches = []
pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
while m := pattern.search(mem, pos):
    pos = m.start() + 1
    matches.append(m[0])

do = True
res = 0
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        n1, n2 = match.split(",")
        res += int(n1[4:]) * int(n2[:-1])

print(res)
