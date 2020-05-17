# https://cses.fi/problemset/task/1669
import sys
from collections import deque

# dont work yet!
def detect_cicle(adj, n):
    visited = [False] * n

    def _bfs(source):
        queue = deque([(source, source)])
        visited[source] = True

        while queue:
            node, prev = queue.pop()

            for neig in adj[node]:
                if neig == source and prev != source:
                    print("Cycle!")
                    print(node, neig, neig == source, prev)
                if visited[neig] or neig == node:
                    continue

                visited[neig] = True
                queue.appendleft((neig, node))

    for node in range(n):
        if visited[node]:
            continue
        _bfs(node)


def main():
    n, m = map(int, sys.stdin.readline().split())
    adjency = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)

    detect_cicle(adjency, n)


if __name__ == "__main__":
    main()