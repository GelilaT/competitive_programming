class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        cur_color = image[sr][sc]
        def dfs(row, col, visited):

            if cur_color != image[row][col]:
                return 
            image[row][col] = color
            visited.add((row,col))
            for row_change,col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    # image[new_row][new_col] = color
                    dfs(new_row, new_col, visited)

        dfs(sr, sc, set())
        return image