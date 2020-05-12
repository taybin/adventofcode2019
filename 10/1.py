from math import gcd

with open('input') as f:
    lines = f.readlines()

# lines = [
#     ".#..#",
#     ".....",
#     "#####",
#     "....#",
#     "...##",
# ]
# lines = [
#     "......#.#.",
#     "#..#.#....",
#     "..#######.",
#     ".#.#.###..",
#     ".#..#.....",
#     "..#....#.#",
#     "#..#....#.",
#     ".##.#..###",
#     "##...#..#.",
#     ".#....####",
# ]

asteroids = {}

max_y = 0
max_x = len(lines[0])
for l in lines:
    x = 0
    for c in l:
        if c == '#':
            asteroids[(x, max_y)] = 0
        x += 1
    max_y += 1


def vectors(a):
    vec = []
    for o in asteroids.keys():
        if o == a:
            continue
        v = (o[0]-a[0], o[1]-a[1])
        common = gcd(v[0], v[1])
        if common != 0 and common != 1:
            v = (int(v[0]/common), int(v[1]/common))
        vec.append(v)
    return set(vec)


for a in asteroids.keys():
    asteroids[a] = len(vectors(a))

print(asteroids)
print(max(asteroids.values()))
