from pyhelper.pyimport import grid_to_dict
capital_letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
grid = grid_to_dict('2019/input/day20_input.txt', set(['.'] + capital_letters))

teleports = {}
for pos, char in grid.items():
    if grid.get(pos) in capital_letters:
        for dir in [1, -1, 1j, -1j]:
            if grid.get(pos - dir) in capital_letters and grid.get(pos + dir) == '.':
                label = (grid[pos - dir] + grid[pos]) if dir in [1, 1j] else (grid[pos] + grid[pos - dir])
                if label == 'AA':
                    starting_pos = pos + dir
                elif label == 'ZZ':
                    ending_pos = pos + dir
                else:
                    teleports[pos + dir] = label
teleport_reverse = {}
for pos, label in teleports.items():
    if label not in teleport_reverse:
        teleport_reverse[label] = set([pos])
    else:
        teleport_reverse[label].add(pos)

positions_seen = set([starting_pos])
paths = [[starting_pos]]
while ending_pos not in positions_seen:
    paths_next = []
    for path in paths:
        for dir in [-1j, 1j, -1, 1]:
            next_pos = path[-1] + dir
            if grid.get(next_pos) == '.' and next_pos not in positions_seen:
                paths_next.append(path + [next_pos])
                positions_seen.add(next_pos)
        if path[-1] in teleports:
            teleport_destination = [loc for loc in teleport_reverse[teleports[path[-1]]] if loc != path[-1]][0]
            paths_next.append(path + [teleport_destination])
            positions_seen.add(teleport_destination)
    paths = paths_next
print(len(paths[0]) - 1)

positions_seen = set(tuple(0, starting_pos))
paths = [[0, starting_pos]]
while ending_pos not in positions_seen:
    paths_next = []
    for path in paths:
        for dir in [-1j, 1j, -1, 1]:
            next_pos = path[-1] + dir
            if grid.get(next_pos) == '.' and next_pos not in positions_seen:
                paths_next.append(path + [next_pos])
                positions_seen.add(next_pos)
        if path[-1] in teleports:
            teleport_destination = [loc for loc in teleport_reverse[teleports[path[-1]]] if loc != path[-1]][0]
            paths_next.append(path + [teleport_destination])
            positions_seen.add(teleport_destination)
    paths = paths_next
print(len(paths[0]) - 1)