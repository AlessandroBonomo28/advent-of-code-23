"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

"""
1. estrai semi
2. estrai mappe
3. conversione:

logica conversione (esempio):

seed-to-soil map:
50 98 2
52 50 48

soil    seed
50 51 | 98 99 |
52 99 | 50 97 |

map(seed-to-soil-ranges, 50) -> 52
map(seed-to-soil-ranges, 51) -> 53
map(seed-to-soil-ranges, 98) -> 50
map(seed-to-soil-ranges, 99) -> 51
map(seed-to-soil-ranges, 100) -> 100
"""

import time


def map(ranges, value):
    for range in ranges:
        dest_range_start = range[0]
        source_range_start = range[1]
        range_length = range[2]
        if value >= source_range_start and value < source_range_start + range_length:
            return dest_range_start + value - source_range_start
    return value

def get_location(maps,seed):
    soil = map(maps["seed-to-soil"], seed)
    fertilizer = map(maps["soil-to-fertilizer"], soil)
    water = map(maps["fertilizer-to-water"], fertilizer)
    light = map(maps["water-to-light"], water)
    temperature = map(maps["light-to-temperature"], light)
    humidity = map(maps["temperature-to-humidity"], temperature)
    location = map(maps["humidity-to-location"], humidity)
    return location

seeds = []

# map range: [destination range start, source range start, range lenght]
maps = {} # key: map name, value: list of ranges [[0, 15,3 ], [37, 52, 3], [2, 39, 3]]



reading_map = False
line_count = 0
with open("input.txt") as f:
    for line in f:
        if line_count ==0:
            seeds = line.split(":")[1].strip().split(" ")
            seeds = [int(x) for x in seeds]
        elif "map" in line:
            reading_map = True
            map_name = line.split(" map")[0]
            maps[map_name] = []
        elif reading_map and not len(line.strip()) == 0:
            maps[map_name].append([int(x) for x in line.strip().split(" ")])
        elif len(line.strip()) == 0:
            reading_map = False
        line_count += 1


print("seeds",seeds)
"""
for map_name in maps:
    print(map_name)
    for i in range(len(maps[map_name])):
        print(maps[map_name][i])"""

#print("map example", map(maps["seed-to-soil"], 98))
start_time = time.time()
min_location = get_location(maps, seeds[0])
seed_index = 0
seed_range_start = 0
for seed in seeds:
    if seed_index % 2 == 0:
        seed_range_start = seed
    else:
        time_seed_start = time.time()
        for i in range(0, seed):
            i_seed = seed_range_start + i
            location = get_location(maps, i_seed)
            #print(f"location of seed {i_seed} is {location}")
            if location < min_location:
                min_location = location
        #print("")
        exec_seed_time = time.time() - time_seed_start
        exec_seed_time = time.strftime('%H:%M:%S', time.gmtime(exec_seed_time))
        print(f"seed {seed} done with min location {min_location} in time {exec_seed_time}")
    seed_index += 1
    print(f"Progress {seed_index//2}/{len(seeds)//2}")
    
print("min location", min_location)
total_time = time.time() - start_time
total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
print(f"Total time: {total_time}")