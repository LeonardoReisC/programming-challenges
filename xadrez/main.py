import sys

PIECES = 'pnbqr'


def check(x, y, board):
    def inner(func, *args, **kwargs):
        return func(x, y, board, *args, **kwargs)
    return inner


def check_horizontal_vertical(x, y, board, opponents: str):
    # horizontal
    for i in range(y, 1, -1):
        slot = board[x][i]
        if slot in ['k', 'K']:
            continue
        if slot != '.':
            if slot in opponents:
                return True
            break

    for i in range(y, 10):
        slot = board[x][i]
        if slot in ['k', 'K']:
            continue
        if board[x][i] != '.':
            if board[x][i] in opponents:
                return True
            break

    # vertical
    for i in range(x, 1, -1):
        slot = board[i][y]
        if slot in ['k', 'K']:
            continue
        if slot != '.':
            if slot in opponents:
                return True
            break

    for i in range(x, 10):
        slot = board[i][y]
        if slot in ['k', 'K']:
            continue
        if slot != '.':
            if slot in opponents:
                return True
            break

    return False


def check_diagonals(x, y, board, opponents: str):
    i, j = x, y

    for k in (-1, 1):
        tshold = (1, 10)
        for l in (-1, 1):  # noqa
            while i not in tshold and j not in tshold:
                slot = board[i][j]
                if slot in ['k', 'K']:
                    i += k
                    j += l
                    continue
                if slot != '.':
                    if slot in opponents:
                        return True
                    break
                i += k
                j += l

            i, j = x, y

    return False


def check_Ls_slot(x, y, board, opponents: str):
    for i in (x - 2, x - 1, x + 1, x + 2):
        for j in (y - 2, y - 1, y + 1, y + 2):

            slot = board[i][j]
            if slot in opponents:
                return True

    return False


def check_frst_diagonal(x, y, board, opponents: str):
    d = -1 if opponents.islower() else 1

    has_opponent1 = board[x + d][y - 1] in opponents
    has_opponent2 = board[x + d][y + 1] in opponents

    if has_opponent1 or has_opponent2:
        return True

    return False


stdin = list(sys.stdin)
games = [stdin[i:i + 8] for i in range(0, len(stdin), 9)]

for game_number in range(0, len(games) - 1):
    board = ['0' * 12, '0' * 12]
    for line in games[game_number]:
        line = line.strip()
        board.append(f'00{line}00')
    board.extend(['0' * 12, '0' * 12])

    king = 'white'
    is_in_check = False

    for i in range(2, 10):
        king_w = board[i].find('k')
        king_b = board[i].find('K')

        if not abs(king_w - king_b):
            continue

        places = sorted([king_w, king_b])
        if not places[0] + 1:
            places.pop(0)

        for j in places:
            # king found
            king = 'white'
            opponents = PIECES
            if board[i][j].islower():
                king = 'black'
                opponents = opponents.upper()

            # decorator
            in_check = check(i, j, board)

            if (
                in_check(check_horizontal_vertical, opponents[3:]) or  # noqa
                in_check(check_diagonals, opponents[2:4]) or  # noqa
                in_check(check_Ls_slot, opponents[1]) or  # noqa
                in_check(check_frst_diagonal, opponents[0])
            ):
                is_in_check = True
                break

        if is_in_check:
            break
    if is_in_check:
        print(f'Game #{game_number+1}: {king} king is in check.')
    else:
        print(f'Game #{game_number+1}: no king is in check.')
