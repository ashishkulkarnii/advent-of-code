def get_tuples_from_sec(s: str) -> list[tuple[int, int, int]]:
    s = s.split("\n")[1:]
    res = []
    for line in s:
        dst, src, n = line.split()
        res.append((int(src), int(dst), int(n)))
    res.sort(key=lambda x: x[1])
    return res


def get_prev_metric(mapping: list[tuple[int, int, int]], metric: int) -> int:
    prev_metric = None
    for src, dst, n in mapping:
        if dst <= metric < dst + n:
            prev_metric = src + (metric - dst)
            break
        if dst > metric:
            break
    if prev_metric == None:
        prev_metric = metric
    return prev_metric


with open("input.txt", "r") as f:
    (
        seeds_planted,
        seed_soil,
        soil_fertiliser,
        fertiliser_water,
        water_light,
        light_temp,
        temp_humidity,
        humidity_loc,
    ) = f.read().split("\n\n")

seed_ranges = list(map(int, seeds_planted.split(": ")[1].split()))
seed_ranges = [(seed_ranges[i], seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]
seed_ranges.sort(key=lambda x: x[0])

seed_soil = get_tuples_from_sec(seed_soil)
soil_fertiliser = get_tuples_from_sec(soil_fertiliser)
fertiliser_water = get_tuples_from_sec(fertiliser_water)
water_light = get_tuples_from_sec(water_light)
light_temp = get_tuples_from_sec(light_temp)
temp_humidity = get_tuples_from_sec(temp_humidity)
humidity_loc = get_tuples_from_sec(humidity_loc)

loc = -1
found = False

while not found:
    loc += 1
    
    humidity = get_prev_metric(humidity_loc, loc)
    temp = get_prev_metric(temp_humidity, humidity)
    light = get_prev_metric(light_temp, temp)
    water = get_prev_metric(water_light, light)
    fertiliser = get_prev_metric(fertiliser_water, water)
    soil = get_prev_metric(soil_fertiliser, fertiliser)
    seed = get_prev_metric(seed_soil, soil)

    for seed_num, n in seed_ranges:
        if seed_num <= seed < seed_num + n:
            found = True
            break

print(loc)
