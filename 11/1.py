from collections import defaultdict, deque
import sys

from intcode import VM

with open('input') as f:
    ops = f.read().split(',')
ops = {i: int(ops[i]) for i in range(0, len(ops))}

area = defaultdict(int)
position = (100, 20)
direction = '^'
area[position] = 1


def print_area():
    print("===================================================")
    min_x = min([int(s[0]) for s in area.keys()])
    max_x = max([int(s[0]) for s in area.keys()])
    min_y = min([int(s[1]) for s in area.keys()])
    max_y = max([int(s[1]) for s in area.keys()])
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) == position:
                sys.stdout.write(direction)
            elif area[(x, y)] == 1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")


def move_forward():
    global position
    if direction == '^':
        position = (position[0], position[1] - 1)
    elif direction == '>':
        position = (position[0] + 1, position[1])
    elif direction == 'v':
        position = (position[0], position[1] + 1)
    elif direction == '<':
        position = (position[0] - 1, position[1])


def turn(choice):
    global direction
    cycle = ['^', '>', 'v', '<']
    if choice == 0:
        direction = cycle[cycle.index(direction) - 1]
    elif choice == 1:
        if direction == '<':
            direction = '^'
        else:
            direction = cycle[cycle.index(direction) + 1]


painted = set()
vm = VM(ops.copy(), deque())
print_area()
while not vm.exited:
    assert len(vm.inputs) == 0
    assert len(vm.outputs) == 0
    vm.inputs.append(area[position])
    vm.run()
    if vm.exited:
        break
    paint = vm.outputs.popleft()
    choice = vm.outputs.popleft()
    area[position] = paint
    painted.add(position)
    turn(choice)
    move_forward()
print_area()


print("Done")
