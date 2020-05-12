with open('input') as f:
    lines = f.readlines()

# lines = ["R8,U5,L5,D3","U7,R6,D4,L4"]
# lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
# lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
wires = []
steps_c = []

for line in lines:
    cmds = line.split(',')
    x = 0
    y = 0
    wire = []
    steps = 0
    point_steps = {}
    for c in cmds:
        direction = c[0]
        distance = int(c[1:]) + 1
        if direction == 'U':
            for new_y in range(y+1, y+distance):
                wire.append((x, new_y))
                steps = steps + 1
                if (x, new_y) not in point_steps:
                    point_steps[(x, new_y)] = steps
                y = new_y
        elif direction == 'D':
            for new_y in range(y-1, y-distance, -1):
                wire.append((x, new_y))
                steps = steps + 1
                if (x, new_y) not in point_steps:
                    point_steps[(x, new_y)] = steps
                y = new_y
        elif direction == 'R':
            for new_x in range(x+1, x+distance):
                wire.append((new_x, y))
                steps = steps + 1
                if (new_x, y) not in point_steps:
                    point_steps[(new_x, y)] = steps
                x = new_x
        elif direction == 'L':
            for new_x in range(x-1, x-distance, -1):
                wire.append((new_x, y))
                steps = steps + 1
                if (new_x, y) not in point_steps:
                    point_steps[(new_x, y)] = steps
                x = new_x
    wires.append(set(wire))
    steps_c.append(point_steps)
crosses = set.intersection(*wires)
distances = [sum([c[(x, y)] for c in steps_c]) for x, y in crosses]
distances.sort()
print(distances)
