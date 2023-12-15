def hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


with open("input.txt") as f:
    strings = f.read().replace("\n", "").split(",")

res = 0
for s in strings:
    res += hash(s)

print(res)
