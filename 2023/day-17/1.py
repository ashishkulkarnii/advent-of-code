with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

i, j = 0, 0

def move(i, j, dir, cost, steps_in_dir=0):
    banned_dir = None
    if steps_in_dir == 3:
        banned_dir = dir
    move(i, j + 1)
    
