# https://cses.fi/problemset/task/1192/
# hint: https://www.youtube.com/watch?v=KiCBXu4P-2Y
import sys
from collections import deque


# it works tho
def count_rooms(grid, shape):
    x, y = shape
    visited = [[False] * y for _ in range(x)]

    def _bfs_grid(i, j):
        x_move = [-1, 1, 0, 0]
        y_move = [0, 0, 1, -1]

        queue = deque([(i, j)])  
        visited[i][j] = True

        while queue:
            i, j = queue.pop()

            for k in range(4):
                ii = i + x_move[k]
                jj = j + y_move[k]

                # check for grid bounds and same type (.)
                if (ii >= x or jj >= y) or (ii < 0 or jj < 0) or (grid[i][j] != grid[ii][jj]):
                    continue
                if visited[ii][jj]:
                    continue

                visited[ii][jj] = True
                queue.appendleft((ii, jj))
        
    n_rooms = 0
    for i in range(x):
        for j in range(y):
            if grid[i][j] == "." and not visited[i][j]:
                _bfs_grid(i, j)
                n_rooms = n_rooms + 1

    return n_rooms


def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = []

    for _ in range(n):
        row = sys.stdin.readline()
        grid.append(row)
    print(grid)
    print(count_rooms(grid, (n, m)))


if __name__ == "__main__":
    main()