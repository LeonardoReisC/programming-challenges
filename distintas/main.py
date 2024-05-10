import sys


def verify_sequence(text, sub, start=0):
    sum = 0
    if not sub:
        return 1

    for i in range(start, len(text)):
        t = text[i]
        s = sub[0]
        if t == s:
            sum += verify_sequence(text, sub[1:], i+1)

    return sum


if __name__ == '__main__':
    output = ''
    stdin = ''.join(sys.stdin).strip().split()
    n = int(stdin.pop(0))

    for _ in range(n):
        text = stdin.pop(0)
        sub = stdin.pop(0)

        output += f'{verify_sequence(text, sub)}\n'

    print(output.rstrip(), end='')
