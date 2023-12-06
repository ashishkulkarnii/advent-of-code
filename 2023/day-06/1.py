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
    times = list(
        map(
            int,
            re.sub(" +", " ", f.readline()).split(": ")[1].replace("\n", "").split(),
        )
    )
    distances = list(
        map(
            int,
            re.sub(" +", " ", f.readline()).split(": ")[1].replace("\n", "").split(),
        )
    )

num_ways_to_win = 1

for race in range(len(times)):
    ways_to_win = all_possible_wins(times[race], distances[race])
    num_ways_to_win *= len(ways_to_win)

print(num_ways_to_win)
