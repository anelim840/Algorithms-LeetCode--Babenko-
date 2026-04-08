class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(r, c):
            # проверяем границы
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r+1, c) #вниз
            dfs(r-1, c) #вверх
            dfs(r, c+1) #вправо
            dfs(r, c-1) #влево

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count    