with open("input.txt") as f:
    line1 = f.readline().replace("\n", "")
    f.readline()
    lines = f.readlines()

graph = {}

for line in lines:
    start, lr = line.split(" = ")
    left, right = lr[1:-2].split(", ")
    graph[start] = (left, right)

curr = "AAA"
ptr = 0
l = len(line1)

while curr != "ZZZ":
    if line1[ptr % l] == "R":
        curr = graph[curr][1]
    else:
        curr = graph[curr][0]
    ptr += 1

print(ptr)
