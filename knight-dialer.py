class Solution:
    def knightDialer(self, n: int) -> int:
        
        rows, cols = 4, 3
        moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
        def inbound(row, col):
            return 0 <= row < 4 and 0 <= col < 3 and \
            (row, col) != (3, 2) and \
            (row, col) != (3, 0)

        memo = {}
        def dp(row, col, cur):
            
            if not inbound(row, col):
                return 0

            if n == cur:                    
                return 1

            if (row, col, cur) in memo:
                return memo[(row, col, cur)]

            ans = 0
            for row_change, col_change in moves:
                new_row = row + row_change
                new_col = col + col_change

                ans += dp(new_row, new_col, cur + 1)

            memo[(row, col, cur)] = ans
            return memo[(row, col, cur)] % (10 ** 9 + 7)

        res = 0
        for i in range(4):
            for j in range(3):
    
                res += dp(i, j, 1)

        return res % (10 ** 9 + 7)