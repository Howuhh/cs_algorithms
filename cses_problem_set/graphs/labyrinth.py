# https://cses.fi/problemset/task/1193
import sys
import cProfile
from time import time

from pprint import pprint
from collections import deque, defaultdict


# TODO: TIME LIMIT on: 1000x1000, but also works tho
# well, just python, nothing to upgrade really (exact same on c++ would work), 2s time
def shortest_path(grid, shape, start):
    x, y = shape
    
    def _bfs_to_end(ni, nj):
        visited = [[False] * y for _ in range(x)]
        prev = [[None] * y for _ in range(x)]

        queue = deque([(ni, nj)])
        visited[ni][nj] = True
        
        x_move = [-1, 1, 0, 0]
        y_move = [0, 0, 1, -1]
        label = ["U", "D", "R", "L"] 

        while queue:
            i, j = queue.pop()

            if grid[i][j] == "B":
                # reconstruct path
                path = []
                while (i, j) != start:
                    i, j, move = prev[i][j]
                    path.append(move)
                return "".join(path[::-1])

            for k in range(4):
                a, b = i + x_move[k], j + y_move[k]

                # check for bounds/# and visited
                if (a < 0 or b < 0) or (a >= x or b >= y) or (grid[a][b] == "#") or visited[a][b] or prev[a][b]:
                    continue
                
                visited[a][b] = True
                prev[a][b] = (i, j, label[k])

                queue.appendleft((a, b))
        return None
    
    path = _bfs_to_end(*start)

    if path:
        sys.stdout.write("YES\n")
        sys.stdout.write(str(len(path)) + "\n")
        sys.stdout.write(path + "\n")
    else:
        sys.stdout.write("NO\n")


def main():
    stime = time()
    n, m = map(int, sys.stdin.readline().split())
    grid = []

    for _ in range(n):
        grid.append(sys.stdin.readline())

    start = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                start = (i, j)

    shortest_path(grid, (n, m), start)
    print(time() - stime)

if __name__ == "__main__":
    main()
    # cProfile.run("main()")