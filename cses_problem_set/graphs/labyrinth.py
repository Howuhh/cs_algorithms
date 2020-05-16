import sys
from time import time

from pprint import pprint
from collections import deque

# TODO: TIME LIMIT on: 1000x1000, but also works tho
def shortest_path(grid, shape, start):
    x, y = shape
    visited = [[False] * y for _ in range(x)]
    distance = [[0] * y for _ in range(x)]
    prev = [[None] * y for _ in range(x)]

    def _negibors(i, j):
        x_move = [-1, 1, 0, 0]
        y_move = [0, 0, 1, -1]
        label = ["U", "D", "R", "L"] 

        for k in range(4):
            ii = i + x_move[k]
            jj = j + y_move[k]

            if (ii < 0 or jj < 0) or (ii >= x or jj >= y) or (grid[ii][jj] == "#"):
                continue
            yield (ii, jj, label[k])

    def _bfs_to_end(ni, nj):
        queue = deque([(ni, nj)])
        visited[ni][nj] = True

        reached_target, target = False, (None, None)
        while queue and not reached_target:
            i, j = queue.pop()

            for a, b, label in _negibors(i, j):
                if visited[a][b]:
                    continue
                
                visited[a][b] = True
                distance[a][b] = distance[i][j] + 1
                prev[a][b] = (i, j, label)

                queue.appendleft((a, b))

                if grid[a][b] == "B":
                    reached_target, target = True, (a, b)
        
        return target
    
    tx, ty = _bfs_to_end(*start)
    if not tx and not ty:
        print("NO")
        return

    print("YES")
    path, path_dist = [], distance[tx][ty]
    while (tx, ty) != start:
        tx, ty, label = prev[tx][ty]
        path.append(label)

    return path_dist, "".join(path[::-1])


def main():
    startt = time()
    n, m = map(int, sys.stdin.readline().split())
    grid = []

    for _ in range(n):
        grid.append(sys.stdin.readline())
    print(time() - startt)

    startt = time()
    start = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                start = (i, j)
    print(time() - startt)

    startt = time()
    res = shortest_path(grid, (n, m), start)
    if res: [print(arg) for arg in res]
    print(time() - startt)

if __name__ == "__main__":
    main()
