class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count=0
        o_count=0
        col=""
        for index,val in enumerate(board):
            for i in range(len(val)):
                if val[i]=="X":
                    x_count+=1
                elif val[i]=="O":
                    o_count+=1
        if x_count < o_count:
            return False
        if o_count < x_count-1:
            return False
        for i in range(3):
            for j in range(3):
                col+=board[j][i]
            if col=="XXX" and x_count == o_count:
                return False
            elif col=="OOO" and o_count != x_count:
                return False
        for i in range(3):
            if board[i]=="XXX" and x_count == o_count:
                return False
            elif board[i]=="OOO" and o_count != x_count:
                return False
        diagonal=""
        for i in range(3):
            diagonal+=board[i][i]
            if diagonal=="XXX" and x_count == o_count:
                return False
            elif diagonal=="OOO" and o_count != x_count:
                return False
        cross_diagonal=board[0][2]+board[1][1]+board[2][0]
        if cross_diagonal=="XXX" and x_count == o_count:
            return False
        elif cross_diagonal=="OOO" and o_count != x_count:
            return False
        return True
Console
