from math import gcd

with open('2019/input/day10_input.txt', 'r') as file:
    input = [line for line in file.read().splitlines()]
asteroids = set()
for i_line, line in enumerate(input):
    for i_char, char in enumerate(line):
        if char == '#':
            asteroids.add(i_line *1j + i_char)

detectable = {}
for station in asteroids:
    vectors_gcd = set()
    for asteroid in [pos for pos in asteroids if pos != station]:
        vector = station - asteroid
        vector_gcd = gcd(int(vector.real), int(vector.imag))
        vectors_gcd.add(int(vector.real) / vector_gcd + int(vector.imag) / vector_gcd * 1j)
    detectable[station] = len(vectors_gcd)
print(max(detectable.values()))