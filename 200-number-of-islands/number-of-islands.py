class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(r, c):
            # границы
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            # если вода
            if grid[r][c] == "0":
                return
            
            # затираем
            grid[r][c] = "0"

            # 4 направления
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count        