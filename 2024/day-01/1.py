with open("input.txt", "r") as f:
    text = f.read()

l = []
r = []
for line in text.split("\n"):
    l.append(int(line.split("   ")[0]))
    r.append(int(line.split("   ")[-1]))

l.sort()
r.sort()

res = 0
for i, n in enumerate(l):
    res += abs(n - r[i])

print(res)
