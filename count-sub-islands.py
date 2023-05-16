class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < len(grid1) and 0 <= col < len(grid1[0])

        visited = set()
        def dfs(row, col):

            if not inbound(row, col) or (row, col) in visited or grid2[row][col] == 0:
                return True

            visited.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                res = dfs(new_row, new_col) and res
            return res
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] and (i, j) not in visited and dfs(i, j):
                    count += 1
        return count