def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield [int(j) for j in l[i:i + n]]

with open('input') as f:
    chunks = list(divide_chunks(f.read(), 25 * 6))

chunks.reverse()
image = chunks[0]
for chunk in chunks:
    for i in range(len(chunk)):
        if chunk[i] == 2:
            continue
        image[i] = chunk[i]

lines = list(divide_chunks(image, 25))
for l in lines:
    print(''.join([str(i) for i in l]))
