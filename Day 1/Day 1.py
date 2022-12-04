import re


def solve_regex(string):
    N = len(string) // 2 # 1

    return sum(int(a) for a, b in zip(string, string[N:]+string[:N]) if a == b)


with open('input.txt') as f:
    data = f.read().strip()


print(solve_regex(data))
