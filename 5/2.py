import sys


i = 0
ops = []


def get_value(arg, mode):
    if mode == 0:
        return ops[arg]
    elif mode == 1:
        return arg


def get_op(op):
    if op < 100:
        return (op, [0] * 5)
    else:
        s = str(op)
        inst = int(s[-2:])
        modes = [int(x) for x in list(s[:-2][::-1])] + ([0] * 5)
        return (inst, modes)


def handle_op(op, modes):
    global i
    if op == 1:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        ops[arg3] = arg1 + arg2
        print(f"pointer {i}: ADD {arg1}, {arg2}, {arg3}")
        i = i + 4
    elif op == 2:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        ops[arg3] = arg1 * arg2
        print(f"pointer {i}: MUL {arg1}, {arg2}, {arg3}")
        i = i + 4
    elif op == 3:
        val = input("Enter your value: ")
        arg1 = ops[i+1]
        ops[arg1] = int(val)
        print(f"pointer {i}: INPUT {arg1}, {val}")
        i = i + 2
    elif op == 4:
        arg1 = ops[i+1]
        print(f"pointer {i}: OUTPUT {arg1}")
        print(ops[arg1])
        i = i + 2
    elif op == 5:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        if arg1 > 0:
            i = arg2
        else:
            i = i + 3
        print(f"pointer {i}: JIT {arg1}, {arg2}")
    elif op == 6:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        print(f"pointer {i}: JIF {ops[i+1], modes[0]} = {arg1}, {ops[i+2], modes[1]} = {arg2}")
        if arg1 == 0:
            i = arg2
        else:
            i = i + 3
    elif op == 7:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        print(f"pointer {i}: SGT {ops[i+1], modes[0]} = {arg1}, {ops[i+2], modes[1]} = {arg2}, {arg3}")
        if arg1 < arg2:
            ops[arg3] = 1
        else:
            ops[arg3] = 0
        i = i + 4
    elif op == 8:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        if arg1 == arg2:
            ops[arg3] = 1
        else:
            ops[arg3] = 0
        print(f"pointer {i}: SEQ {arg1}, {arg2}, {arg3}")
        i = i + 4
    elif op == 99:
        print(f"pointer {i}: EXIT")
        sys.exit()
    else:
        print(f"ERROR, bad op {i}, {ops[i]}")
        print(ops)
        sys.exit()


with open('input') as f:
    ops = f.read().split(',')
# ops = [3,9,8,9,10,9,4,9,99,-1,8]
# ops = [3,9,7,9,10,9,4,9,99,-1,8]
# ops = [3,3,1108,-1,8,3,4,3,99]
# ops = [3,3,1107,-1,8,3,4,3,99]
# ops = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
ops = [int(op) for op in ops]
print(ops)
while True:
    op = ops[i]
    decoded = get_op(ops[i])
    handle_op(decoded[0], decoded[1])
    if op == 99:
        break
