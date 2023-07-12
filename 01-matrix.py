class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(mat)
        cols = len(mat[0])
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                else:
                    ans[i][j] = -1

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        while queue:
            row, col = queue.popleft()

            for row_change, col_change in directions:

                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    ans[new_row][new_col] = ans[row][col] + 1
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                
        return ans