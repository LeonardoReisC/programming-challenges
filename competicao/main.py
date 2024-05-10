# type: ignore
import sys

PENALTY = 20
CONTESTANT = 0
PROBLEMS_SOLVED = 1
TIME_TAKEN = 2
PENALTIES = 3


def get_index(contestant, data):
    for i in data:
        if i[0] == contestant:
            return data.index(i)
    return 0


output = ''
stdin = list(sys.stdin)
n = int(stdin[0])

competitions = ''.join(stdin[2:]).strip().split('\r\n\r\n')
for i in range(n):
    competition = competitions[i].split('\r\n')
    data = []
    for line in competition:
        info = line.strip().split(' ')
        contestant = int(info[0])
        problem = int(info[1]) - 1
        time = int(info[2])
        msg = info[3]

        if data:
            if not list(filter(lambda x: x[CONTESTANT] == contestant, data)):
                data.append([contestant, '', 0, [0 for _ in range(9)]])
        else:
            data.append([contestant, '', 0, [0 for _ in range(9)]])

        index: int = get_index(contestant, data)

        if str(problem) in data[index][PROBLEMS_SOLVED] or msg in "RUE":
            continue
        elif msg == "I":
            data[index][PENALTIES][problem] += 1
            continue

        data[index][PROBLEMS_SOLVED] += str(problem)
        data[index][TIME_TAKEN] += time

    for info in data:
        for problem in range(9):
            if str(problem) not in info[PROBLEMS_SOLVED]:
                info[PENALTIES][problem] = 0

        info[TIME_TAKEN] += abs(sum(info[PENALTIES]) * 20)

    data.sort(key=lambda x: (len(x[PROBLEMS_SOLVED]),
                             -x[TIME_TAKEN], -x[CONTESTANT]), reverse=True)

    for info in data:
        output += f'{info[CONTESTANT]} {len(info[PROBLEMS_SOLVED])} {info[TIME_TAKEN]}\n'

    if not i + 1 == n:
        output += '\n'

print(output, end='')