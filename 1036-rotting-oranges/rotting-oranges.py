from collections import deque

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

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1