class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row, col):

            area = 1
            visited.add((row,col))
            for row_change,col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    area += dfs(new_row, new_col)
            return area
        
        visited = set()
        max_area = 0
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area