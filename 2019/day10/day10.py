from math import gcd

from pyhelper.pyimport import grid_to_complex_set
asteroids = grid_to_complex_set('2019/input/day10_input.txt', {'#'})

detectable = {}
for station in asteroids:
    vectors_gcd = set()
    for asteroid in [pos for pos in asteroids if pos != station]:
        vector = station - asteroid
        vector_gcd = gcd(int(vector.real), int(vector.imag))
        vectors_gcd.add(int(vector.real) / vector_gcd + int(vector.imag) / vector_gcd * 1j)
    detectable[station] = len(vectors_gcd)
print(max(detectable.values()))