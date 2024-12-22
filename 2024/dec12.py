import numpy as np
 
rows = [line for line in np.loadtxt('2024/input/dec12_input.txt', dtype = str)]
map = {}
for i_row, row in enumerate(rows):
    for i_char in range(len(row)):
        map[i_char + i_row * 1j] = rows[i_row][i_char]

# part 1
price = 0
car_dir = [1, -1, 1j, -1j]
map_seen = []
for pos_start, letter in map.items():
    if pos_start not in map_seen:
        perimeter = 0
        pos_region = [pos_start]
        pos_region_i = 0
        while pos_region_i < len(pos_region):
            for dir in car_dir:
                if map.get(pos_region[pos_region_i] + dir) != letter:
                    perimeter += 1
                elif pos_region[pos_region_i] + dir not in pos_region:
                    pos_region.append(pos_region[pos_region_i] + dir)
            pos_region_i += 1
        map_seen.extend(pos_region)
        price += len(pos_region) * perimeter
print('ans1: ' + str(price))

# part 2
price = 0
car_dir = [1, -1, 1j, -1j]
map_seen = []
for pos_start, letter in map.items():
    if pos_start not in map_seen:
        pos_region = [pos_start]
        pos_region_i = 0
        while pos_region_i < len(pos_region):
            for dir in car_dir:
                if map.get(pos_region[pos_region_i] + dir) == letter and pos_region[pos_region_i] + dir not in pos_region:
                    pos_region.append(pos_region[pos_region_i] + dir)
            pos_region_i += 1
        map_seen.extend(pos_region)
        corners = 0
        for pos in pos_region:
            for x in [-1, 1]:
                for y in [-1j, 1j]:
                    if map.get(pos + x) != letter and map.get(pos + y) != letter:
                        corners += 1
                    if map.get(pos + x) == letter and map.get(pos + y) == letter and map.get(pos + x + y) != letter:
                        corners += 1
        price += len(pos_region) * corners
print('ans2: ' + str(price))