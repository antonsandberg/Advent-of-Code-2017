from itertools import combinations

with open('input.txt') as f:
    data = [[int(y) for y in x.split()] for x in f.readlines()]
diff = 0
for row in data:

    combs = combinations(sorted(row), 2)
    diff += sum(b//a for a, b in combs if b % a == 0)
print(diff)


