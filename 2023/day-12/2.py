with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def get_arrangement(s):
    s = s.strip(".")
    while ".." in s:
        s = s.replace("..", ".")
    return [len(x) for x in s.split(".")]


res = 0

for line in lines:
    s, arrangement = line.split()

    arrangement = list(map(int, arrangement.split(",")))
    arrangement = 5 * arrangement
    total_hash = sum(arrangement)

    s = s + "?" + s + "?" + s + "?" + s + "?" + s
    fixed = s.count("#")
    var = s.count("?")

    no_arrangements = 0
    for i in range(2 ** var):
        p = format(i, f"0{var}b").replace("0", ".").replace("1", "#")
        if p.count("#") != total_hash - fixed:
            print("fail", p)
            continue
        p = list(p)
        s_ = s
        while p:
            s_ = s_.replace("?", p.pop(0), 1)
        print(s_, get_arrangement(s_), arrangement)
        if get_arrangement(s_) == arrangement:
            no_arrangements += 1

    res += no_arrangements

print(res)
