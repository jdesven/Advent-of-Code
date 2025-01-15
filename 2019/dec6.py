with open('2019/input/dec6_input.txt', 'r') as file:
    input = [line.split(')') for line in file.read().splitlines()]

orbitting = {orbit[1]: orbit[0] for orbit in input}

count = 0
for orbit in orbitting:
    cur_orbit = orbit
    while cur_orbit != 'COM':
        cur_orbit = orbitting[cur_orbit]
        count += 1
print(count)

orbitted = {orbit[1]:{} for orbit in input}

for orbit_start in [orbit for orbit in orbitted.keys() if orbit not in orbitting.values()]:
    print(orbit_start)
    dict = {}
    cur_orbit = orbit_start
    while cur_orbit != 'COM':
        orbitted[cur_orbit] = dict
        for key in dict.keys():
            dict[key] += 1
        dict[cur_orbit] = 1
        cur_orbit = orbitting[cur_orbit]
    print(orbitted['G1T'])
    exit()
