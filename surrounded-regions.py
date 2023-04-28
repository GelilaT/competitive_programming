class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        def dfs(row, col):
            if inbound(row, col) and board[row][col] == "O":
                board[row][col] = "V"
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    dfs(new_row, new_col)
            
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)

        for j in range(len(board[0]) - 1):
            dfs(0, j)
            dfs(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"