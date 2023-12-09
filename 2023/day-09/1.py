def generate_triangle(row):
    triangle = [row]
    while not all([i == 0 for i in triangle[-1]]):
        triangle.append(
            [n - triangle[-1][i - 1] for i, n in list(enumerate(triangle[-1]))[1:]]
        )
    return triangle


def extrapolate_next_val(triangle):
    next_val = 0
    for i, row in list(enumerate(triangle))[:0:-1]:
        next_val = next_val + triangle[i - 1][-1]
    return next_val


with open("input.txt", "r") as f:
    lines = f.readlines()

res = 0

for line in lines:
    row = list(map(int, line.strip().split()))
    triangle = generate_triangle(row)
    res += extrapolate_next_val(triangle)

print(res)
