import sys


def get_ints(line):
    return list(map(int, line.strip().split()))


def _3n_plus_1_problem(n):
    i = 1
    while n - 1:
        i += 1
        if not n % 2:
            n /= 2
            continue
        n = 3 * n + 1
    return i


for line in sys.stdin:
    n = 1
    input = get_ints(line)
    a, b = sorted(input)

    for number in range(a, b + 1):
        i = _3n_plus_1_problem(number)
        if i <= n:
            continue
        n = i
    print(*input, n)