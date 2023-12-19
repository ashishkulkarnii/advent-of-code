class Part:
    def __init__(self, s):
        self.cat = dict()
        for category_rating in s[1:-1].split(","):
            self.cat[category_rating[0]] = int(category_rating[2:])

    def evaluate(self, workflow):
        for condition in workflow:
            if "<" in condition:
                if self.cat[condition[0]] < int(condition.split(":")[0][2:]):
                    return condition.split(":")[-1]
                else:
                    pass
            elif ">" in condition:
                if self.cat[condition[0]] > int(condition.split(":")[0][2:]):
                    return condition.split(":")[-1]
                else:
                    pass
            else:
                return condition


with open("input.txt") as f:
    workflows_txt, parts = f.read().split("\n\n")

workflows = dict()
for workflow in workflows_txt.split("\n"):
    name, workflow = workflow.strip().split("{")
    workflows[name] = workflow[:-1].split(",")

parts = parts.split("\n")

res = 0

for part in parts:
    part = Part(part)
    wf = part.evaluate(workflows["in"])
    while wf not in {"A", "R"}:
        wf = part.evaluate(workflows[wf])
    match wf:
        case "A":
            res += sum(part.cat.values())
        case "R":
            pass

print(res)
