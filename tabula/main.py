import sys
import math

if __name__ == '__main__':
    output = ''
    stdin = ''.join(sys.stdin).strip().split('\n')

    for triangle in stdin:
        a, b, c = map(float, triangle.strip().split(' '))

        s = (a + b + c) / 2

        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        try:
            max_radius = round(area / s, 3)
        except ZeroDivisionError:
            max_radius = 0.0

        output += f'the radius of the round table is: {max_radius:.3f}\n'

    print(output.rstrip(), end='')
