class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        arr = [[0 for _ in range(n)] for i in range(m)]
        arr[0][0] = 1
        
        for i in range(m):
            for j in range(n):

                if inbound(i, j - 1):
                    arr[i][j] += arr[i][j - 1]

                if inbound(i - 1, j):
                    arr[i][j] += arr[i - 1][j]

        return arr[-1][-1]