import math

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

l = len(line1)

# # bruteforce
# while not all([curr[-1] == "Z" for curr in currs]):
#     print(currs)
#     if line1[ptr % l] == "R":
#         currs = [graph[curr][1] for curr in currs]
#     else:
#         currs = [graph[curr][0] for curr in currs]
#     ptr += 1

# LCM, may not work in all cases
ptrs = []
for curr in currs:
    ptr = 0
    while curr[-1] != "Z":
        if line1[ptr % l] == "R":
            curr = graph[curr][1]
        else:
            curr = graph[curr][0]
        ptr += 1
    ptrs.append(ptr)

print(ptrs)

res = math.lcm(*ptrs)

print(res)
