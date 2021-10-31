
class Solution:
    def numIslands(self, grid):
        row, col, ret = len(grid), len(grid[0]), 0

        def dfs(x, y):
            grid[x][y] = '0'
            for c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + c[0], y + c[1]
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == '1':
                    dfs(nx, ny)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ret += 1
        return ret

