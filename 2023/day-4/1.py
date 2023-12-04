import re

res = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = re.sub(" +", " ", line)
        card, numbers = line.split(": ")
        winning_numbers, card_numbers = numbers.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split(" ")))
        card_numbers = list(map(int, card_numbers.split(" ")))
        matches = 0
        for n in card_numbers:
            if n in winning_numbers:
                matches += 1
        if matches > 0:
            res += 2 ** (matches - 1)

print(res)