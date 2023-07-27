class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        queue = deque()
        first = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        x, y = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    x, y = i, j
                    break

        first.append((x, y))
        queue.append((x, y, 0))
        grid[x][y] = 2
        while first:

            row, col = first.popleft()
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col, 0))
                    first.append((new_row, new_col))
                    grid[new_row][new_col] = 2


        while queue:
            
            row, col, path = queue.popleft()
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) :
                    if grid[new_row][new_col] == 1:
                        return path

                    elif grid[new_row][new_col] == 0:

                        grid[new_row][new_col] = -1
                        queue.append((new_row, new_col, path + 1))