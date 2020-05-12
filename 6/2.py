with open('input') as f:
    lines = f.readlines()

orbs = {}

# lines = [
#     'COM)B\n',
#     'B)C\n',
#     'C)D\n',
#     'D)E\n',
#     'E)F\n',
#     'B)G\n',
#     'G)H\n',
#     'D)I\n',
#     'E)J\n',
#     'J)K\n',
#     'K)L\n',
#     'K)YOU\n',
#     'I)SAN\n'
# ]

for l in lines:
    split = l.split(')')
    orbs[split[1][:-1]] = split[0]

# print(orbs)
visited = set()
you_count = 0
san_count = 0
base = orbs['YOU']
while base in orbs:
    base = orbs[base]
    visited.add(base)
# print(visited)

base = orbs['SAN']
while base in orbs:
    print(f'SAN {base} to {orbs[base]}')
    base = orbs[base]
    san_count = san_count + 1
    if base in visited:
        common = base
        break

print(san_count)

base = orbs['YOU']
while base in orbs:
    print(f'YOU {base} to {orbs[base]}')
    base = orbs[base]
    you_count = you_count + 1
    if base == common:
        break

print(you_count)
print(you_count + san_count)
