with open("input.txt") as f:
    line1 = f.readline().replace("\n", "")
    f.readline()
    lines = f.readlines()

graph = {}

for line in lines:
    start, lr = line.split(" = ")
    left, right = lr.replace("\n", "")[1:-1].split(", ")
    graph[start] = (left, right)


currs = []
for key in graph.keys():
    if key[-1] == "A":
        currs.append(key)

ptr = 0
l = len(line1)

while not all([curr[-1] == "Z" for curr in currs]):
    if line1[ptr % l] == "R":
        currs = [graph[curr][1] for curr in currs]
    else:
        currs = [graph[curr][0] for curr in currs]
    ptr += 1

print(ptr)
