import sys


def map_ring(x):
    total = 0
    ring = 0

    i = 0
    while i * 6 + total + 1 < x:
        total += 6 * i
        ring += 1
        i += 1

    return ring


def get_coordinate(ring, x):
    if not ring:
        return 0, 0

    number = 1
    for i in range(ring+1):
        number += 6*i
    coord = [ring, 0]

    number -= ring
    if number <= x:
        coord[1] = x - number - ring
        return coord
    coord[1] = -ring

    number -= ring
    if number <= x:
        coord[0] = x - number
        return coord
    coord[0] = 0

    number -= ring
    if number <= x:
        coord[0] = x - number - ring
        coord[1] = number - x
        return coord
    coord = [-ring, 0]

    number -= ring
    if number <= x:
        coord[1] = number - x + ring
        return coord
    coord[1] = ring

    number -= ring
    if number <= x:
        coord[0] = number - x
        return coord
    coord[1] = ring

    number -= ring - 1
    if number <= x:
        coord[0] = number - x + ring - 1
        coord[1] = x - number + 1
        return coord


if __name__ == '__main__':
    output = ''
    stdin = (map(int, ''.join(sys.stdin).strip().split('\n')))

    for number in stdin:
        ring = map_ring(number)
        coord = get_coordinate(ring, number)
        output += '{} {}\n'.format(*coord)

    print(output.rstrip(), end='')
