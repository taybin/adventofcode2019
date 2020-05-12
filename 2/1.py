import sys

with open('input') as f:
    ops = f.read().split(',')
    ops = [int(op) for op in ops]
    ops[1] = 12
    ops[2] = 2

i = 0

def handle_op(op):
  global i
  global ops
  if op == 1:
    ops[ops[i+3]] = ops[ops[i+1]] + ops[ops[i+2]]
    i = i + 4
  elif op == 2:
    ops[ops[i+3]] = ops[ops[i+1]] * ops[ops[i+2]]
    i = i + 4
  if op == 99:
    print(ops)
    sys.exit()

while True:
    op = ops[i]
    handle_op(op)
