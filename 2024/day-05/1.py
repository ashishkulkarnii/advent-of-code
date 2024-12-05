from collections import defaultdict


with open("input.txt", "r") as f:
    data = f.read()

rules, updates = data.split("\n\n")
rules = [[int(p) for p in rule.split("|")] for rule in rules.split("\n")]
updates = [[int(pno) for pno in orders.split(",")] for orders in updates.split("\n")]

rule_dict = defaultdict(list)
for p1, p2 in rules:
    rule_dict[p1].append(p2)

ans = 0
for update in updates:
    n = len(update)
    good_update = True
    for i in range(n):
        p1 = update[i]
        for j in range(i + 1, n):
            p2 = update[j]
            if p2 not in rule_dict[p1]:
                good_update = False
                break
    if good_update:
        ans += update[n//2]
print(ans)
