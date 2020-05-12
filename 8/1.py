def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield [int(j) for j in l[i:i + n]]

with open('input') as f:
    chunks = list(divide_chunks(f.read(), 25 * 6))

fewest_zero_i = 0
fewest_zeros = 99
for i in range(len(chunks)):
    print('i', i)
    zero_count = chunks[i].count(0)
    print('zeros', zero_count)
    if zero_count < fewest_zeros:
        print('fewer!')
        fewest_zero_i = i
        fewest_zeros = zero_count

print(fewest_zero_i, fewest_zeros)

v = chunks[fewest_zero_i].count(1) * chunks[fewest_zero_i].count(2)
print(v)
