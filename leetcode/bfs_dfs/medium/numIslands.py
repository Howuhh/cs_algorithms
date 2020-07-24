from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    self.dfs(i, j, grid, rows, cols, visited)

        return count

    def dfs(self, x, y, grid, rows, cols, visited):
        x_move = [-1, 1, 0, 0]
        y_move = [0, 0, 1, -1]

        for i in range(4):
            xx = x + x_move[i]
            yy = y + y_move[i]

            if (xx < 0 or xx >= rows) or (yy < 0 or yy >= cols):
                continue

            if grid[xx][yy] == "1" and not visited[xx][yy]:
                visited[xx][yy] = True
                self.dfs(xx, yy, grid, rows, cols, visited)


        
        