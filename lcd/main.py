import sys


def get_lcd(digits: str, size: int):
    disable = {
        '0': 'd',
        '1': 'abdeg',
        '2': 'bf',
        '3': 'be',
        '4': 'aeg',
        '5': 'ce',
        '6': 'c',
        '7': 'bdeg',
        '8': '',
        '9': 'e',
    }
    rows = 2 * size + 3

    lcd: list[str] = ['' for _ in range(rows)]

    for digit in digits:
        lcd[0] += ' '
        if 'a' not in disable[digit]:
            lcd[0] += '-' * size
        else:
            lcd[0] += ' ' * size
        lcd[0] += ' '

        lcd[0] += ' '

        for i in range(1, size+1):
            if 'b' not in disable[digit]:
                lcd[i] += '|{}'.format(' ' * size)
            else:
                lcd[i] += ' ' * (size + 1)

        for i in range(1, size+1):
            if 'c' not in disable[digit]:
                lcd[i] += '|'
            else:
                lcd[i] += ' '
            lcd[i] += ' '

        lcd[size + 1] += ' '
        if 'd' not in disable[digit]:
            lcd[size + 1] += '-' * size
        else:
            lcd[size + 1] += ' ' * size
        lcd[size + 1] += ' '
        lcd[size + 1] += ' '

        for i in range(size + 2, rows-1):
            if 'e' not in disable[digit]:
                lcd[i] += '|{}'.format(' ' * size)
            else:
                lcd[i] += ' ' * (size + 1)

        for i in range(size + 2, rows-1):
            if 'f' not in disable[digit]:
                lcd[i] += '|'
            else:
                lcd[i] += ' '
            lcd[i] += ' '

        lcd[rows - 1] += ' '
        if 'g' not in disable[digit]:
            lcd[rows - 1] += '-' * size
        else:
            lcd[rows - 1] += ' ' * size
        lcd[rows - 1] += ' '
        lcd[rows - 1] += ' '

    return lcd


if __name__ == '__main__':
    output = ''
    stdin = ''.join(sys.stdin).strip().split('\n')

    s, n = stdin.pop(0).strip().split(' ')

    while s != '0' and n != '0':
        lcd = get_lcd(n, int(s))

        for row in lcd:
            output += f'{row.rstrip()}\n'

        output += '\n'

        s, n = stdin.pop(0).strip().split(' ')

    print(output.rstrip())
