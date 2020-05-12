with open('input') as f:
    lines = f.readlines()

orbs = {}

# lines = [
#     'COM)B',
#     'B)C',
#     'C)D',
#     'D)E',
#     'E)F',
#     'B)G',
#     'G)H',
#     'D)I',
#     'E)J',
#     'J)K',
#     'K)L'
# ]

for l in lines:
    split = l.split(')')
    orbs[split[1][:-1]] = split[0]

print(orbs)
direct = len(orbs)
# leaves = set(orbs.keys()) - set(orbs.values())
# print(leaves)
indirect = 0
for l in orbs.keys():
    base = orbs[l]
    # print(f'{l} orbits {base}')
    while base in orbs:
        # print(f'{base} orbits {orbs[base]}')
        base = orbs[base]
        indirect = indirect + 1

print(direct)
print(indirect)
print(direct + indirect)
