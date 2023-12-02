res = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        _, turns = line.split(":")
        turns = turns.split("; ")

        max_r, max_g, max_b = 0, 0, 0

        for handful in turns:
            handful = handful.split(", ")
            for color in handful:
                quantity = int(color.split()[0])
                if "red" in color:
                    max_r = max(max_r, quantity)
                elif "green" in color:
                    max_g = max(max_g, quantity)
                elif "blue" in color:
                    max_b = max(max_b, quantity)
        
        res += max_r * max_g * max_b

print(res)
