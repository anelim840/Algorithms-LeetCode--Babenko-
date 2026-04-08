class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0

        while q:
            size = len(q) 

            for i in range(size):
                r, c = q.popleft()

                if r+1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    fresh -= 1
                    q.append((r+1, c))

                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    fresh -= 1
                    q.append((r-1, c))

                if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    fresh -= 1
                    q.append((r, c+1))

                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    fresh -= 1
                    q.append((r, c-1))

            time += 1 
       
        if fresh > 0:
            return -1

        if time > 0:
            return time - 1

        return 0