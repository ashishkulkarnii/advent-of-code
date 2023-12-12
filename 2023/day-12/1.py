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
    total_hash = sum(arrangement)

    fixed = s.count("#")
    var = s.count("?")

    all_permutations = list(
        filter(
            lambda x: x.count("#") == total_hash - fixed,
            list(
                format(i, f"0{var}b").replace("0", ".").replace("1", "#")
                for i in range(2 ** var)
            ),
        )
    )

    no_arrangements = 0
    for p in all_permutations:
        p = list(p)
        s_ = s
        while p:
            s_ = s_.replace("?", p.pop(0), 1)
        print(s_, get_arrangement(s_), arrangement)
        if get_arrangement(s_) == arrangement:
            no_arrangements += 1

    res += no_arrangements

print(res)
