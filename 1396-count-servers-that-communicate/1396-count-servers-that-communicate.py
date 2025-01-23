class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        count = 0
        rowCount = [0] * m
        colCount = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    rowCount[i] += 1
                    colCount[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rowCount[i] > 1 or colCount[j] > 1:
                        count += 1 
                          
        return count