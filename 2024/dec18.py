with open('2024/input/dec18_input.txt', 'r') as file:
    input = [int(line[0]) + int(line[1]) * 1j for line in [line.split(',') for line in file.read().splitlines()]]

def construct_empty_map():
    map = {}
    for x in range(71):
        for y in range(71):
            map[x + y * 1j] = '.'
    return map

def bfs_shortest_path(map):
    coords_seen = {0 + 0j}
    potential_paths = [[0 + 0j]]
    path_i = 0
    dirs = [-1, 1, -1j, 1j]
    while path_i < len(potential_paths):
        path = potential_paths[path_i]
        for dir in dirs:
            next_pos = path[-1] + dir
            if next_pos == 70 + 70j:
                solution = set(path)
                path_i = len(potential_paths)
            elif map.get(next_pos) == '.' and next_pos not in coords_seen:
                coords_seen.add(next_pos)
                potential_paths.append(path + [next_pos])
        path_i += 1
    return solution if 'solution' in locals() else set()

# part 1
map = construct_empty_map()
for coord in input[:1024]:
    map[coord] = '#'
print('ans1: ' + str(len(bfs_shortest_path(map))))

# part 2
map = construct_empty_map()
valid_path = bfs_shortest_path(map)
for i_byte, byte in enumerate(input):
    map[byte] = '#'
    if byte in valid_path:
        valid_path = bfs_shortest_path(map)
        if len(valid_path) == 0:
            blocking_byte = byte

print('ans2: ' + str(int(blocking_byte.real)) + ',' + str(int(blocking_byte.imag)))