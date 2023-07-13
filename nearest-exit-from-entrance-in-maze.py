class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set((entrance[0], entrance[1]))
        rows = len(maze)
        cols = len(maze[0])
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        # ans = 0
        while queue:
            row, col, ans = queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col):
                    if (new_row, new_col) not in visited and maze[new_row][new_col] == ".":
                        queue.append((new_row, new_col, ans + 1))
                        visited.add((new_row, new_col))

                elif (row, col) != (entrance[0], entrance[1]):
                    return ans
        
        return -1