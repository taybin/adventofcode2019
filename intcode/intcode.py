import sys
import logging


opLogger = logging.getLogger("ops")
logging.basicConfig(level=logging.INFO)


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
        self.exited = False

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

    def add(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        arg3 = self.get_position(self.ops[self.i+3], modes[2])
        self.ops[arg3] = arg1 + arg2
        opLogger.debug(f"{self.ops[self.i]}: ADD {arg1}, {arg2}, {arg3}")
        self.i = self.i + 4

    def multiply(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        arg3 = self.get_position(self.ops[self.i+3], modes[2])
        self.ops[arg3] = arg1 * arg2
        opLogger.debug(f"{self.ops[self.i]}: MUL {arg1}, {arg2}, {arg3}")
        self.i = self.i + 4

    def input(self, modes):
        val = input("Enter your value: ")
        arg1 = self.get_position(self.ops[self.i+1], modes[0])
        self.ops[arg1] = int(val)
        opLogger.debug(f"{self.ops[self.i]}: INPUT {arg1}, {val}")
        self.i = self.i + 2

    def output(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        opLogger.debug(f"{self.ops[self.i]}: OUTPUT {arg1}")
        print("Output: ", arg1)
        self.i = self.i + 2

    def jump_if_not_zero(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        opLogger.debug(f"{self.ops[self.i]}: JNZ {arg1}, {arg2}")
        if arg1 != 0:
            self.i = arg2
        else:
            self.i = self.i + 3

    def jump_if_false(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        opLogger.debug(f"{self.ops[self.i]}: JIF {arg1}, {arg2}")
        if arg1 == 0:
            self.i = arg2
        else:
            self.i = self.i + 3

    def set_if_greater_than(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        arg3 = self.get_position(self.ops[self.i+3], modes[2])
        opLogger.debug(f"{self.ops[self.i]}: SIGT {arg1}, {arg2}, {arg3}")
        if arg1 < arg2:
            self.ops[arg3] = 1
        else:
            self.ops[arg3] = 0
        self.i = self.i + 4

    def set_if_equal_to(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        arg2 = self.get_value(self.ops[self.i+2], modes[1])
        arg3 = self.get_position(self.ops[self.i+3], modes[2])
        opLogger.debug(f"{self.ops[self.i]}: SIEQ {arg1}, {arg2}, {arg3}")
        if arg1 == arg2:
            self.ops[arg3] = 1
        else:
            self.ops[arg3] = 0
        self.i = self.i + 4

    def set_relative_base(self, modes):
        arg1 = self.get_value(self.ops[self.i+1], modes[0])
        self.rel_base = self.rel_base + arg1
        opLogger.debug(f"{self.ops[self.i]}: SETR {arg1}")
        self.i = self.i + 2

    def exit(self):
        opLogger.debug(f"{self.ops[self.i]}: EXIT")
        self.exited = True
        print("EXITING")


    def handle_op(self, op, modes):  # noqa: C901
        if op == 1:
            self.add(modes)
        elif op == 2:
            self.multiply(modes)
        elif op == 3:
            self.input(modes)
        elif op == 4:
            self.output(modes)
        elif op == 5:
            self.jump_if_not_zero(modes)
        elif op == 6:
            self.jump_if_false(modes)
        elif op == 7:
            self.set_if_greater_than(modes)
        elif op == 8:
            self.set_if_equal_to(modes)
        elif op == 9:
            self.set_relative_base(modes)
        elif op == 99:
            self.exit()
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
ops = {i: int(ops[i]) for i in range(0, len(ops))}

vm = VM(ops.copy())
vm.run()
