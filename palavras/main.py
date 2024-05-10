import sys

stdin = "".join(list(sys.stdin)).strip().split('\n\n')

n_cases = int(stdin[0])

output = ''


def hunting_words(grid: list[str]):
    def find_word(x: int, word: str, reverse: bool = False):
        def track(x, y, word: str, dx, dy):

            coords_x = [x+(dx*i) for i in range(2, len(word))]
            coords_y = [y+(dy*i) for i in range(2, len(word))]

            for i in range(0, len(word)-2):
                _x = coords_x[i]
                _y = coords_y[i]
                letter = grid[_x][_y]

                if letter == '*' or letter != word[i+2]:
                    return False

            return True

        if reverse:
            word = word[-1::-1]

        n = grid[x].count(word[0])
        if not n:
            return None

        previous_index = 0
        for _ in range(n):
            y = grid[x].index(word[0], previous_index)
            if len(word) == 1:
                return x, y

            neighbours = (
                (x-1, y-1), (x-1, y), (x-1, y+1),
                (x, y-1), (x, y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1),
            )
            for i, j in neighbours:
                if grid[i][j] == word[1]:
                    dx = i-x
                    dy = j-y
                    if track(x, y, word, dx, dy):
                        if reverse:
                            return x+dx*(len(word)-1), y+dy*(len(word)-1)
                        return x, y

            previous_index = y+1

    return find_word


for n in range(1, n_cases+1):
    case = stdin[n].strip().split('\n')

    rows, columns = map(int, case[0].split(' '))
    grid = ['*'*(columns+2)]
    grid.extend([f'*{item.lower()}*' for item in case[1: rows+1]])
    grid.extend(['*'*(columns+2)])

    n_words = int(case[rows+1])
    words = [item.lower() for item in case[rows+2:]]
    find_word = hunting_words(grid)

    for word in words:
        coords = []
        for i in range(1, rows+1):
            coord = find_word(i, word) or find_word(i, word, reverse=True)
            if coord:
                coords.append(coord)

        coords.sort(key=lambda x: (x[0], x[1]))
        output += f'{coords[0][0]} {coords[0][1]}\n'
    output += '\n'

print(output.rstrip(), end='\n')
