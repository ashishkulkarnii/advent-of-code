import re


def all_possible_wins(time, record_distance):
    distances = []
    for charge_t in range(0, time + 1):
        speed = charge_t
        time_remaining = time - charge_t
        distance = speed * (time_remaining)
        if distance > record_distance:
            distances.append(distance)
    return distances


with open("input.txt") as f:
    time = int(re.sub(" +", "", f.readline()).split(":")[1].replace("\n", ""))
    distance = int(re.sub(" +", "", f.readline()).split(":")[1].replace("\n", ""))

ways_to_win = all_possible_wins(time, distance)
num_ways_to_win = len(ways_to_win)

print(num_ways_to_win)
