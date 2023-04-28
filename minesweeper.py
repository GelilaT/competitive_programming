class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [(0, 1),(0, -1), (1, 0), (-1, 0), (1, 1),(1, -1), (-1, -1),(-1, 1)]
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row, col):

            if board[row][col] == "M":
                board[row][col] = "X"
                return
            
            elif board[row][col] == "E":
                neighbours = 0
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                        neighbours += 1
                
                if neighbours:
                    curr = board[row][col]
                    if isinstance(curr, int):
                        board[row][col] = str(neighbours + int(curr))
                    else:
                        board[row][col] = str(neighbours)

                else:
                    board[row][col] = "B"
                    for row_change, col_change in directions:
                        new_row = row + row_change
                        new_col = col + col_change
                        if inbound(new_row, new_col):
                            dfs(new_row, new_col)

        dfs(click[0], click[1])
        return board