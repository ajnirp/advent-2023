with open(0) as file:
    data = [line.strip() for line in file.readlines()]

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

seeds = list(map(int, data[0].split()[1:]))

active = None
for line in data[2:]:
    if not line:
        continue
    if line.startswith('seed'):
        active = seed_to_soil
    elif line.startswith('soil'):
        active = soil_to_fertilizer
    elif line.startswith('fertilizer'):
        active = fertilizer_to_water
    elif line.startswith('water'):
        active = water_to_light
    elif line.startswith('light'):
        active = light_to_temperature
    elif line.startswith('temperature'):
        active = temperature_to_humidity
    elif line.startswith('humidity'):
        active = humidity_to_location
    else:
        dst, src, width = list(map(int, line.split()))
        active[src] = (dst, width)

def step(val, range_map):
    for src, (dst, width) in range_map.items():
        if 0 <= val - src <= width:
            return dst + val - src
    return val

def seed_to_location(seed):
    soil = step(seed, seed_to_soil)
    fertilizer = step(soil, soil_to_fertilizer)
    water = step(fertilizer, fertilizer_to_water)
    light = step(water, water_to_light)
    temperature = step(light, light_to_temperature)
    humidity = step(temperature, temperature_to_humidity)
    location = step(humidity, humidity_to_location)
    return location

print(min(map(seed_to_location, seeds)))
