import re

input = "136818-685979"

count = 0

double_re = r"(.)\1"


def only_two(x, n):
    return (
        re.search(x * 2, n) and
        not re.search(x * 3, n) and
        not re.search(x * 4, n) and
        not re.search(x * 5, n) and
        not re.search(x * 6, n)
    )


def valid(n):
    if not re.search(double_re, n):
        return False
    value = n[0]
    found_only_two = False
    for x in n:
        if x < value:
            return False
        if only_two(x, n):
            found_only_two = True
        value = x
    return found_only_two


print("valid")
print(valid("122345"))
print(valid("111122"))
print(valid("112233"))
print("not valid")
print(valid("111111"))
print(valid("111123"))
print(valid("123435"))
print(valid("135679"))
print(valid("223450"))
print(valid("123789"))
print(valid("123444"))
print(valid("111222"))
print(valid("123333"))


for n in range(136818, 685979 + 1):
    if valid(str(n)):
        count += 1

print(count)
