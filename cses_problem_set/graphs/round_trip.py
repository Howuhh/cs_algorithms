# https://cses.fi/problemset/task/1669
import sys
from collections import deque


# dont work yet!
def detect_cicle(adj, n):
    visited = [False] * n
    prev = [None] * n

    # dfs in python not a good choice (rec limit)
    def _bfs(source):
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.pop()

            for neig in adj[node]:
                if visited[neig]:
                    if neig == prev[node]:
                        continue
                    else:
                        # if visited and not paret -> cycle (start, end)
                        return (neig, node)

                visited[neig] = True
                prev[neig] = node
                queue.appendleft(neig)
               
        return False
    
    # start bfs from every unvisited node
    cycle = False
    for node in range(n):
        if visited[node]:
            continue
        if cycle:
            break
        cycle = _bfs(node)
    
    # cycle path
    if cycle:
        start, end = cycle

        path = deque()
        while start is not None or end is not None:
            if prev[start] is not None:
                path.append(start)
                start = prev[start]

            if prev[end] is not None:
                path.appendleft(end)
                end = prev[end]
               
            if path[0] == path[-1]:
                break

            # # if from end/start path of same length
            if start == end:
                path.append(start)
                path.appendleft(end)
                break
        
        # thhh, no one will see that!
        start, end = 0, len(path) - 1
        while path[start] == path[end]:
            start += 1
            end -= 1
        start, end = start - 1, end + 1
        
        path = list(path)[start:end+1]

        print(len(path))
        print(*[i + 1 for i in path])
    else:
        print("IMPOSSIBLE")


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