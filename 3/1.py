with open('input') as f:
    lines = f.readlines()

#lines = ["R8,U5,L5,D3","U7,R6,D4,L4"]
#lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
#lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
wires = []

for line in lines:
    cmds = line.split(',')
    x = 0
    y = 0
    wire = []
    for c in cmds:
        direction = c[0]
        distance = int(c[1:]) + 1
        if direction == 'U':
            for new_y in range(y, y+distance):
                wire.append((x, new_y))
                y = new_y
        elif direction == 'D':
            for new_y in range(y, y-distance, -1):
                wire.append((x, new_y))
                y = new_y
        elif direction == 'R':
            for new_x in range(x, x+distance):
                wire.append((new_x, y))
                x = new_x
        elif direction == 'L':
            for new_x in range(x, x-distance, -1):
                wire.append((new_x, y))
                x = new_x
    wires.append(set(wire))
crosses = set.intersection(*wires)
distances = [abs(x)+abs(y) for x,y in crosses]
distances.sort()
print(distances)
