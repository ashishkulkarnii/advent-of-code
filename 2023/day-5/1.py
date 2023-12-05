res = float("inf")


def get_tuples_from_sec(s: str) -> list[tuple[int, int, int]]:
    s = s.split("\n")[1:]
    res = []
    for line in s:
        dest, src, n = line.split()
        res.append((int(src), int(dest), int(n)))
    res.sort(key=lambda x: x[0])
    return res


def get_metric(mapping: list[tuple[int, int, int]], prev_metric: int) -> int:
    metric = None
    for start, end, n in mapping:
        if start <= prev_metric < start + n:
            metric = end + (prev_metric - start)
            break
        if start > prev_metric:
            break
    if metric == None:
        metric = prev_metric
    return metric


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

seeds_planted = list(map(int, seeds_planted.split(": ")[1].split()))

seed_soil = get_tuples_from_sec(seed_soil)
soil_fertiliser = get_tuples_from_sec(soil_fertiliser)
fertiliser_water = get_tuples_from_sec(fertiliser_water)
water_light = get_tuples_from_sec(water_light)
light_temp = get_tuples_from_sec(light_temp)
temp_humidity = get_tuples_from_sec(temp_humidity)
humidity_loc = get_tuples_from_sec(humidity_loc)

for seed in seeds_planted:
    soil = get_metric(seed_soil, seed)

    fertiliser = get_metric(soil_fertiliser, soil)

    water = get_metric(fertiliser_water, fertiliser)

    light = get_metric(water_light, water)

    temp = get_metric(light_temp, light)

    humidity = get_metric(temp_humidity, temp)

    loc = get_metric(humidity_loc, humidity)

    res = min(res, loc)

print(res)