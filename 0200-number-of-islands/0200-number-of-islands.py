class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):

            if visited[row][col]:
                return 

            visited[row][col] = 1
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands



        

        
        
       