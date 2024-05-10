import sys

stdin = "".join(list(sys.stdin)).strip().split('\n')
output = ''

n_cases = int(stdin[0])


def reverse(number):
    reverse = 0
    while number:
        reverse *= 10
        reverse += number % 10
        number = int(number / 10)

    return reverse


for n in range(1, n_cases+1):
    number_of_sums = 0

    number = int(stdin[n])
    while True:
        reverse_number = reverse(number)

        if not number - reverse_number and number_of_sums:
            output += f'{number_of_sums} {reverse_number}\n'
            break

        number += reverse_number
        number_of_sums += 1


print(output.rstrip(), end='\n')
