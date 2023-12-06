input_file = "input.txt"


def get_first_digit(s: str) -> int:
    for c in s:
        if c.isdigit():
            return int(c)


res = 0

with open(input_file) as f:
    for line in f.readlines():
        res += get_first_digit(line) * 10 + get_first_digit(line[::-1])

print(res)
