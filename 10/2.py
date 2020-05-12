from math import gcd, atan2
import operator

with open('input') as f:
    lines = f.readlines()
station = (17, 22)

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
    return list(set(vec))


def get_next_vector(station):
    while len(asteroids) > 1:
        tan = {(x, y): atan2(x, y) for x, y in vectors(station)}
        s = sorted(tan.items(), key=operator.itemgetter(1), reverse=True)
        non_neg_idx = 0
        for i in range(len(s)):
            if s[i][1] >= 0.0:
                non_neg_idx = i
                break
        fixed = s[non_neg_idx:] + s[:non_neg_idx]
        for t in fixed:
            v = t[0]
            yield v


def get_next_asteroid(station):
    for v in get_next_vector(station):
        p = (station[0] + v[0], station[1] + v[1])
        while p not in asteroids:
            p = (p[0] + v[0], p[1] + v[1])
        yield p


def delete_asteroids(station):
    while len(asteroids) > 1:
        for a in get_next_asteroid(station):
            del asteroids[a]
            yield a


a = list(delete_asteroids(station))[199]
print(a)
print(a[0] * 100 + a[1])
