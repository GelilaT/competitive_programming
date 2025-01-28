class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if grid[i][j] == 0:
                return 0

            val = grid[i][j]
            grid[i][j] = 0
            for x, y in directions:
                val += dfs(i + x, j + y)

            return val

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans