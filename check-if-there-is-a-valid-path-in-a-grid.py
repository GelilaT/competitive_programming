class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions = {
            1 : [(0, -1),(0, 1)],
            2 : [(-1, 0),(1, 0)],
            3 : [(0, -1), (1, 0)],
            4 : [(1, 0), (0, 1)],
            5 : [(0, -1), (-1, 0)],
            6 : [(-1, 0), (0, 1)]
        }
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def inbound(row, col):
            return (0 <= row < rows) and (0 <= col < cols)
        
        def dfs(row, col):

            if (row, col) == (rows - 1, cols - 1):
                return True


            for row_change, col_change in directions[grid[row][col]]:

                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col):

                    if (-row_change, -col_change) in directions[grid[new_row][new_col]] and visited[new_row][new_col] == 0:
                        
                        visited[new_row][new_col] = 1
                        found = dfs(new_row, new_col)
                        if found :
                            return True

                # return False
        return dfs(0, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # directions = defaultdict(list)
        # directions[1] = [(0,1),(0,-1)]
        # directions[2] = [(1,0),(-1,0)]
        # directions[3] = [(0,1),(1,0)]
        # directions[4] = [(-1,0), (0,1)]
        # directions[5] = [(0,1),(-1,0)]
        # directions[6] = [(-1,0),(0,1)]

        # def dfs(row,col):
        #     if (row,col) in visited:
        #         return
        #     visited.add((row,col))
        #     for row_change,col_change in directions[grid[row][col]]:
        #         new_row += row_change
        #         new_col += col_change
        #         if inbound(new_row,new_col) and (new_row,new_col) not in visited:
        #             dfs(new_row, new_col)

        # visited = set()
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):