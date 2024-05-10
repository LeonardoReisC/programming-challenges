import sys


class Node:
    def __init__(self) -> None:
        self.neighbours: list[Node] = []
        self.visited = False
        self.color = False

    def add(self, node):
        self.neighbours.append(node)


def is_bicolorable(node):
    queue: list[Node] = []
    queue.append(node)

    while queue:
        root = queue.pop(0)
        root.visited = True

        for neighbour in root.neighbours:
            if not neighbour.visited:
                neighbour.color = not root.color
                queue.append(neighbour)
            else:
                if neighbour.color == root.color:
                    return False

    return True


if __name__ == '__main__':
    output = ''
    stdin = "".join(sys.stdin).strip().split('\n')
    stdin.reverse()

    n = int(stdin.pop())
    while n:
        e = int(stdin.pop())
        nodes: list[Node] = [Node() for _ in range(n)]

        for _ in range(e):
            x, y = map(int, stdin.pop().split(' '))
            nodes[x].add(nodes[y])
            nodes[y].add(nodes[x])

        if is_bicolorable(nodes[0]):
            output += 'BICOLORABLE.\n'
        else:
            output += 'NOT BICOLORABLE.\n'

        n = int(stdin.pop())

    print(output.rstrip())
