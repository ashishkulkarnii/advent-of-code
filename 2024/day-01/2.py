from collections import Counter

with open("input.txt", "r") as f:
    text = f.read()

l = []
r = []
for line in text.split("\n"):
    l.append(int(line.split("   ")[0]))
    r.append(int(line.split("   ")[-1]))

rc = Counter(r)

res = 0
for n in l:
    res += n * rc[n]

print(res)
