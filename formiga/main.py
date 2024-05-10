import sys


def calculate_last(x):
    i = 1
    total = 0

    while total < x:
        total += 8 * i
        i += 1
    total -= 8 * (i-1) - 1

    return [1, 2*(i-1) - 1], total


def get_sec_coordenate(sec, initial, coord):
    if sec == initial:
        return

    coord[1] += 1
    initial += 1
    if sec == initial:
        return

    initial += coord[1] - 1
    if sec <= initial:
        coord[0] = coord[1] - (initial - sec)
        return
    coord[0] = coord[1]

    initial += coord[0] - 1
    if sec <= initial:
        coord[1] = initial - sec + 1
        return
    coord[1] = 1

    coord[0] += 1
    initial += 1
    if sec == initial:
        return

    initial += coord[0] - 1
    if sec <= initial:
        coord[1] = coord[0] - (initial - sec)
        return
    coord[1] = coord[0]

    initial += coord[1] - 1
    if sec <= initial:
        coord[0] = initial - sec + 1
        return
    coord[0] = 1


if __name__ == '__main__':
    output = ''

    stdin = ''.join(sys.stdin).strip().split('\n')
    sec = int(stdin.pop(0))

    while sec:
        coord, initial = calculate_last(sec)

        get_sec_coordenate(sec, initial, coord)

        output += '{} {}\n'.format(*coord)

        sec = int(stdin.pop(0))

    print(output.rstrip(), end='')
