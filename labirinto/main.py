import sys


def dump_maze(maze, symbol, row, col):
    if symbol == '/':
        maze[row][col+2] = 1
        maze[row+1][col+1] = 1
        maze[row+2][col] = 1
    else:
        maze[row][col] = 1
        maze[row+1][col+1] = 1
        maze[row+2][col+2] = 1


def flood_fill(maze, x, y, nrow, ncol):
    maze[x][y] = 1

    nflooded = 0
    is_a_cycle = True

    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)

        if x - 1 < 0 or x + 1 >= nrow or y - 1 < 0 or y + 1 >= ncol:
            is_a_cycle = False

        nflooded += 1

        if x - 1 >= 0 and not maze[x-1][y]:
            maze[x-1][y] = 1
            queue.append((x-1, y))

        if y + 1 < ncol and not maze[x][y+1]:
            maze[x][y+1] = 1
            queue.append((x, y+1))

        if x + 1 < nrow and not maze[x+1][y]:
            maze[x+1][y] = 1
            queue.append((x+1, y))

        if y - 1 >= 0 and not maze[x][y-1]:
            maze[x][y-1] = 1
            queue.append((x, y-1))

    if not is_a_cycle:
        return 0
    return nflooded // 3


if __name__ == '__main__':
    stdin = "".join(sys.stdin).strip().split('\n')
    output = ''
    maze_number = 0

    ncol, nrow = map(int, stdin.pop(0).split(' '))

    while ncol and nrow:
        maze = [[0 for _ in range(3*ncol)] for _ in range(3*nrow)]
        maze_number += 1

        cycles = []

        for x in range(nrow):
            row = list(stdin.pop(0).strip())
            for y in range(ncol):
                dump_maze(maze, row[y], 3*x, 3*y)

        for x in range(3*nrow):
            for y in range(3*ncol):
                if not maze[x][y]:
                    cycle = flood_fill(maze, x, y, 3*nrow, 3*ncol)
                    if cycle:
                        cycles.append(cycle)
        cycles.sort(reverse=True)

        output += f'Maze #{maze_number}:\n'
        if cycles:
            output += f'{len(cycles)} Cycles; the longest has length {cycles[0]}.\n\n'
        else:
            output += f'There are no cycles.\n\n'

        ncol, nrow = map(int, stdin.pop(0).split(' '))

    print(output.rstrip(), end='\n\n')
