# FIXME: This is a very slow solution. I'll try to find a better one later.

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

seed_ranges = list(map(int, seeds_planted.split(": ")[1].split()))

seed_soil = get_tuples_from_sec(seed_soil)
soil_fertiliser = get_tuples_from_sec(soil_fertiliser)
fertiliser_water = get_tuples_from_sec(fertiliser_water)
water_light = get_tuples_from_sec(water_light)
light_temp = get_tuples_from_sec(light_temp)
temp_humidity = get_tuples_from_sec(temp_humidity)
humidity_loc = get_tuples_from_sec(humidity_loc)

from_soil = dict()
from_fertiliser = dict()
from_water = dict()
from_light = dict()
from_temp = dict()
from_humidity = dict()
from_loc = dict()

for i in range(0, len(seed_ranges), 2):
    print(i, "/", len(seed_ranges))

    start_seed = seed_ranges[i]
    num = seed_ranges[i + 1]
    for i in range(num):
        print("\t", i, "/", num)

        seed = start_seed + i

        soil = get_metric(seed_soil, seed)
        if soil in from_soil:
            loc = from_soil[soil]
        else:
            fertiliser = get_metric(soil_fertiliser, soil)
            if fertiliser in from_fertiliser:
                loc = from_fertiliser[fertiliser]
            else:
                water = get_metric(fertiliser_water, fertiliser)
                if water in from_water:
                    loc = from_water[water]
                else:
                    light = get_metric(water_light, water)
                    if light in from_light:
                        loc = from_light[light]
                    else:
                        temp = get_metric(light_temp, light)
                        if temp in from_temp:
                            loc = from_temp[temp]
                        else:
                            humidity = get_metric(temp_humidity, temp)
                            if humidity in from_humidity:
                                loc = from_humidity[humidity]
                            else:
                                loc = get_metric(humidity_loc, humidity)
                                from_humidity[humidity] = loc
                            from_temp[temp] = loc
                        from_light[light] = loc
                    from_water[water] = loc
                from_fertiliser[fertiliser] = loc
            from_soil[soil] = loc

        res = min(res, loc)

print(res)
