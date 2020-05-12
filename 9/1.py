import sys
import logging


def get_op(op):
    if op < 100:
        return (op, [0] * 5)
    else:
        s = str(op)
        inst = int(s[-2:])
        modes = [int(x) for x in list(s[:-2][::-1])] + ([0] * 5)
        return (inst, modes)


class VM:
    def __init__(self, ops):
        self.i = 0
        self.ops = ops
        self.rel_base = 0

    def get_value(self, arg, mode):
        if mode == 0:
            return self.ops.get(arg, 0)
        elif mode == 1:
            return arg
        elif mode == 2:
            return self.ops.get(arg + self.rel_base, 0)

    def get_position(self, arg, mode):
        if mode == 0:
            return arg
        elif mode == 1:
            return arg
        elif mode == 2:
            return arg + self.rel_base

    def handle_op(self, op, modes):
        if op == 1:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            arg3 = self.get_position(self.ops[self.i+3], modes[2])
            self.ops[arg3] = arg1 + arg2
            print(f"pointer {self.i}: ADD {arg1}, {arg2}, {arg3}")
            self.i = self.i + 4
        elif op == 2:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            arg3 = self.get_position(self.ops[self.i+3], modes[2])
            self.ops[arg3] = arg1 * arg2
            print(f"pointer {self.i}: MUL {arg1}, {arg2}, {arg3}")
            self.i = self.i + 4
        elif op == 3:
            print(self.ops)
            print("INPUT MODES", modes, self.rel_base)
            val = input("Enter your value: ")
            arg1 = self.get_position(self.ops[self.i+1], modes[0])
            print('arg1', arg1)
            self.ops[arg1] = int(val)
            print(f"pointer {self.i}: INPUT {arg1}, {val}")
            self.i = self.i + 2
        elif op == 4:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            print(f"pointer {self.i}: OUTPUT {arg1}")
            print(arg1)
            self.i = self.i + 2
        elif op == 5:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            if arg1 != 0:
                self.i = arg2
            else:
                self.i = self.i + 3
            print(f"pointer {self.i}: JIT {arg1}, {arg2}")
        elif op == 6:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            print(f"pointer {self.i}: JIF {self.ops[self.i+1], modes[0]} = {arg1}, {self.ops[self.i+2], modes[1]} = {arg2}")
            if arg1 == 0:
                self.i = arg2
            else:
                self.i = self.i + 3
        elif op == 7:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            arg3 = self.get_position(self.ops[self.i+3], modes[2])
            print(f"pointer {self.i}: SGT {self.ops[self.i+1], modes[0]} = {arg1}, {self.ops[self.i+2], modes[1]} = {arg2}, {arg3}")
            if arg1 < arg2:
                self.ops[arg3] = 1
            else:
                self.ops[arg3] = 0
            self.i = self.i + 4
        elif op == 8:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            arg2 = self.get_value(self.ops[self.i+2], modes[1])
            arg3 = self.get_position(self.ops[self.i+3], modes[2])
            if arg1 == arg2:
                self.ops[arg3] = 1
            else:
                self.ops[arg3] = 0
            print(f"pointer {self.i}: SEQ {arg1}, {arg2}, {arg3}")
            self.i = self.i + 4
        elif op == 9:
            arg1 = self.get_value(self.ops[self.i+1], modes[0])
            self.rel_base = self.rel_base + arg1
            print(f"pointer {self.i}: SET_REL {arg1}")
            self.i = self.i + 2

        elif op == 99:
            print(f"pointer {self.i}: EXIT")
            sys.exit()
        else:
            print(f"ERROR, bad op {self.i}, {self.ops[self.i]}")
            print(self.ops)
            sys.exit()

    def run(self):
        while True:
            op = self.ops[self.i]
            decoded = get_op(self.ops[self.i])
            self.handle_op(decoded[0], decoded[1])
            if op == 99:
                break


with open('input') as f:
    ops = f.read().split(',')
#ops = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# ops = [1102,34915192,34915192,7,4,7,99,0]
# ops = [104,1125899906842624,99]
ops = [int(op) for op in ops]
print(ops)
ops = {i: ops[i] for i in range(0, len(ops))}

vm = VM(ops.copy())
vm.run()
