class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n
        ans = []
        def bfs(row, col):
            queue = deque([[row, col, 0]])
            visited = set((row, col))
            while queue:
                px, py, count = queue.popleft()
                if px == n - 1 and py == n - 1:
                   ans.append(count + 1)
                for row_change, col_change in directions:
                    new_row = px + row_change
                    new_col = py + col_change
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                        visited.add((new_row, new_col))
                        queue.append([new_row, new_col, count + 1])
        if not grid[0][0] and not grid[n - 1][n - 1]:
            bfs(0, 0)
        print(ans)
        if ans:
            return ans[0]
        else:
            return -1