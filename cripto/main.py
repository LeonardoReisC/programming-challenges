import sys

plaintext = 'the quick brown fox jumps over the lazy dog'.split(' ')
output = ''


def equals_plaintext(sentence, index, i=0, decoder=None):
    if decoder is None:
        decoder = {}

    if i == len(plaintext):
        return decoder

    len_decrypted_text = len(plaintext[i])
    len_encrypted_text = len(sentence[index])

    if len_decrypted_text == len_encrypted_text:
        for j in range(len_encrypted_text):
            encrypted_letter = sentence[index][j]
            decrypted_letter = plaintext[i][j]

            decrypted = decoder.get(encrypted_letter)
            decrypted = decrypted and decrypted != decrypted_letter
            if decrypted:
                return {}
            decoder[encrypted_letter] = decrypted_letter

        index += 1
        i += 1
        return equals_plaintext(sentence, index, i, decoder)
    else:
        return {}


stdin = "".join(list(sys.stdin)).strip().split('\n\n')

cases = int(stdin[0])

for case in range(cases):
    lines = stdin[case+1].split('\n')

    number_of_words = [len(line.split(' ')) for line in lines]
    sentence = stdin[case+1].replace('\n', ' ').split(' ')

    for i in range(len(sentence)):
        decoder = equals_plaintext(sentence, i)
        if decoder:
            line = 0
            word_count = 0
            for word in sentence:
                word_count += 1
                decrypted_word = ''
                for letter in word:
                    decrypted_word += decoder[letter]
                output += f'{decrypted_word}'

                if word_count == number_of_words[line]:
                    output += '\n'
                    line += 1
                    word_count = 0
                else:
                    output += ' '
            break
    else:
        output += 'No solution.\n'
    output += '\n'

output = output.rstrip()
print(output)
