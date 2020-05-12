def calc(n):
    print(1, n)
    if n <= 0:
        print(2)
        return 0
    print(3)
    new = int(n / 3) - 2
    print(4, new)
    total = new + calc(new)
    if total <= 0:
        total = 0
    print(5, total)
    return total


with open('input') as file:
    sum = 0
    for line in file.readlines():
        sum += calc(int(line))
    print(sum)
