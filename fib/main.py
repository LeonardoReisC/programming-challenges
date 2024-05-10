import sys

stdin = ("".join(list(sys.stdin)).strip().split('\n'))
output = ''

fibonacci = [1, 2]


def get_index_of_number_or_first_greater(x):
    for i in range(len(fibonacci)):
        if fibonacci[i] >= x:
            return i


def extend_fibonacci(x):
    if fibonacci[-1] > x:
        return

    prev_1 = fibonacci[-2]
    prev_2 = fibonacci[-1]

    fibonacci.append(prev_1 + prev_2)
    extend_fibonacci(x)


def fibonacci_between(a, b):
    extend_fibonacci(b)

    inf = get_index_of_number_or_first_greater(a)
    sup = get_index_of_number_or_first_greater(b)

    numbers_between = sup - inf

    if not numbers_between:
        if a in fibonacci or b in fibonacci:
            numbers_between += 1
    else:
        if b in fibonacci:
            numbers_between += 1

    return numbers_between


for numbers in stdin:
    a, b = map(int, numbers.split(' '))

    if not a and not b:
        break

    output += f'{fibonacci_between(a, b)}\n'

print(output.rstrip(), end='')
