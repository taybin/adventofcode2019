import sys

i = 0
ops = []
n = 0
v = 0

def handle_op(op):
  global i
  global n
  global v
  if op == 1:
    ops[ops[i+3]] = ops[ops[i+1]] + ops[ops[i+2]]
    i = i + 4
  elif op == 2:
    ops[ops[i+3]] = ops[ops[i+1]] * ops[ops[i+2]]
    i = i + 4
  if op == 99:
    if ops[0] == 19690720:
        print(100 * n + v)
        sys.exit()


for n in range(99):
    for v in range(99):
        with open('input') as f:
            ops = f.read().split(',')
            ops = [int(op) for op in ops]
            ops[1] = n
            ops[2] = v
            i = 0
            while True:
                op = ops[i]
                handle_op(op)
                if op == 99:
                    break
