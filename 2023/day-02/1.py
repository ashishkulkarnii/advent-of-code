r, g, b = 12, 13, 14

res = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        game, turns = line.split(":")
        game_id = int(game.split()[1])
        turns = turns.split("; ")

        for handful in turns:
            handful = handful.split(", ")
            for color in handful:
                quantity = int(color.split()[0])
                if "red" in color and quantity > r:
                    game_id = 0
                    break
                elif "green" in color and quantity > g:
                    game_id = 0
                    break
                elif "blue" in color and quantity > b:
                    game_id = 0
                    break
        
        res += game_id

print(res)
