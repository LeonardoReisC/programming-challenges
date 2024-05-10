import sys

stdin = ("".join(list(sys.stdin)).strip().split('\n'))
output = ''


def number_of_carry_operations(a, b, carry=0):
    if not a and not b:
        return 0

    r1 = a % 10
    r2 = b % 10

    a = int(a / 10)
    b = int(b / 10)

    if carry + r1 + r2 >= 10:
        carry = 1
    else:
        carry = 0

    return carry + number_of_carry_operations(a, b, carry)


for numbers in stdin:
    a, b = map(int, numbers.split(' '))
    if not a and not b:
        break

    number_of_operations = number_of_carry_operations(a, b)

    output += '{} carry operation{}.\n'.format(
        'No' if not number_of_operations else number_of_operations,
        's' if number_of_operations > 1 else ''
    )

print(output.rstrip())
