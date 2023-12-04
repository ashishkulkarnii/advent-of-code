import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    quantity = [1 for _ in lines]
    for i, line in enumerate(lines):
        line = re.sub(" +", " ", line)
        card, numbers = line.split(": ")
        winning_numbers, card_numbers = numbers.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split(" ")))
        card_numbers = list(map(int, card_numbers.split(" ")))
        q_ptr = 1
        for n in card_numbers:
            if n in winning_numbers:
                quantity[i + q_ptr] += quantity[i]
                q_ptr += 1

print(sum(quantity))
