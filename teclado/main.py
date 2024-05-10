import sys

output = ''

keyboard = '\u00601234567890-=\n\u0009QWERTYUIOP[]\\\nASDFGHJKL;\'\nZXCVBNM,./'

stdin = "".join(sys.stdin).strip().split('\n')

for line in stdin:
    for letter in line:
        key = ' '
        if letter in keyboard:
            left_key = keyboard[keyboard.index(letter)-1]
            if left_key == '\n':
                key = letter
            else:
                key = left_key

        output += key
    output += '\n'

print(output.rstrip(), end='\n')
