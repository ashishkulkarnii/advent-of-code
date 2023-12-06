input_file = "input.txt"
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_first_and_digit(s: str) -> tuple[int, int]:
    nums = []

    for i, c in enumerate(s):
        if c.isdigit():
            nums.append(int(c))
        else:
            for j, n in enumerate(numbers):
                if s[i:i+len(n)] == n:
                    nums.append(j + 1)

    return (nums[0], nums[-1])


res = 0

with open(input_file) as f:
    for line in f.readlines():
        first, last = get_first_and_digit(line)
        res += first * 10 + last

print(res)
