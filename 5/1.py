import sys


i = 0
ops = []


def get_value(arg, mode):
    if mode == 0:
        return ops[arg]
    elif mode == 1:
        return arg


def get_opt(op):
    if op < 100:
        return (op, [0] * 5)
    else:
        s = str(op)
        inst = int(s[-2:])
        modes = [int(x) for x in list(s[:-2][::-1])] + ([0] * 5)
        return (inst, modes)


def handle_op(op, modes=None):
    global i
    if op == 1:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        ops[arg3] = arg1 + arg2
        i = i + 4
    elif op == 2:
        arg1 = get_value(ops[i+1], modes[0])
        arg2 = get_value(ops[i+2], modes[1])
        arg3 = ops[i+3]
        ops[arg3] = arg1 * arg2
        i = i + 4
    elif op == 3:
        val = input("Enter your value: ")
        ops[ops[i+1]] = int(val)
        i = i + 2
    elif op == 4:
        print(ops[ops[i+1]])
        i = i + 2
    if op == 99:
        sys.exit()


with open('input') as f:
    ops = f.read().split(',')
    ops = [int(op) for op in ops]
    while True:
        op = ops[i]
        decoded = get_opt(ops[i])
        handle_op(decoded[0], decoded[1])
        if op == 99:
            break
